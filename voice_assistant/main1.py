from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import os
# from fastapi.middleware.cors import CORSMiddleware
import whisper
from transformers import pipeline
import sys
sys.path.append(r"C:\AI_Coop\Homework\Week3\voice_assistant\CosyVoice")  # 根据你的实际路径调整
from CosyVoice import CozyVoice
import tempfile

app = FastAPI()

# ========== Step 1: ASR ==========
#Load Whipser model(第一次会下载模型)
asr_model = whisper.load_model("small")

def transcribe_audio(audio_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(audio_bytes)
        tmp_file.flush()
        result = asr_model.transcribe(tmp_file.name)
    text = result["text"].strip()
    print(f"[ASR Output] User said: {text}")
    return text

# ========== Step 2: LLM ==========
# 载入轻量级文本生成模型（占内存少，方便调试）
llm = pipeline("text-generation", model="distilgpt2")

# 简单对话历史，保存最近 5 轮
conversation_history = []

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://127.0.0.1:5500"],  # 或者 ["*"] 仅开发时用
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

def generate_response(user_text):
    conversation_history.append({"role": "user", "text": user_text})
    # 构造 prompt（只保留最近 5 轮对话）
    prompt = ""
    for turn in conversation_history[-5:]:
        prompt += f"{turn['role']}: {turn['text']}\n"
    # 调用 LLM
    outputs = llm(prompt, max_new_tokens=100)
    full_output = outputs[0]["generated_text"]
    # 取"assitant:"之后的部分
    bot_response = full_output.split("assistant:")[-1].strip()
    conversation_history.append({"role": "assistant", "text": bot_response})
    print(f"[LLM Output] Assistant said: {bot_response}")
    return bot_response


# ========== Step 3: TTS ==========
tts_engine = CozyVoice()

def synthesize_speech(text, filename="response.wav"):
    tts_engine.generate(text, output_file=filename)
    return filename

# ========== Step 4: 整合到 API ==========
@app.post("/chat/")
async def chat_endpoint(file: UploadFile = File(...)):
    # 读取上传的音频
    print("📥 Received request")
    audio_bytes = await file.read()
    
    # ASR → LLM → TTS
    # Step 2: ASR：转录成文字(语音识别)
    user_text = transcribe_audio(audio_bytes)
    print("[ASR Output] User said:", user_text, flush=True)  # 调试输出

    # Step 3: LLM（生成回复）
    bot_text = generate_response(user_text)
    print("[LLM Output] Bot said:", bot_text, flush=True)

    # (合成语音)
    audio_path = synthesize_speech(bot_text)
    

    # 返回 response.wav 的完整路径（推荐使用绝对路径）(返回wav文件)
    # file_path = os.path.abspath("response.wav")
    return FileResponse(audio_path, media_type="audio/wav")
    