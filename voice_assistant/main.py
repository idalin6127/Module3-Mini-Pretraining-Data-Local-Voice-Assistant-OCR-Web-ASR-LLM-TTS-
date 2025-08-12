from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.concurrency import run_in_threadpool
from fastapi.middleware.cors import CORSMiddleware  # <- 导入CORS中间件
import os

from asr import transcribe_audio
from llm import conv_manager
from tts import synthesize_speech

app = FastAPI()

# 在这里添加CORS中间件配置，确保跨域请求被允许
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # "*" 表示允许所有来源，如果有前端固定地址，可以写具体的url，比如["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "API is running"}


@app.post("/chat/")
async def chat_endpoint(file: UploadFile = File(...)):
    audio_bytes = await file.read()

    
    # user_text = transcribe_audio(audio_bytes)
    # bot_text = conv_manager.generate_response(user_text)
    # audio_path = synthesize_speech(bot_text)

    try:
        # 语音转文字
        user_text = await run_in_threadpool(transcribe_audio, audio_bytes)
        print(f"[ASR output] User said: {user_text}")  # 识别内容打印
        
        
        # LLM 生成回复
        bot_text = await run_in_threadpool(conv_manager.generate_response, user_text)
        # 打印 LLM 回复
        print(f"[DEBUG] LLM generated reply: {bot_text}")  # 机器人回复打印

        # 如果回复是空的，给兜底
        if not bot_text.strip():
            bot_text = "I didn't catch that. Could you please repeat?"
            print("[DEBUG] LLM reply was empty, used fallback response.")

        # 机器人回复打印（最终的）
        print(f"[LLM output] Bot said: {bot_text}")
        
        # TTS 合成语音（返回字节）
        audio_path = await run_in_threadpool(synthesize_speech, bot_text)
        print(f"[TTS output] Audio file ready: {audio_path}")

        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found at {audio_path}")

        return FileResponse(audio_path, media_type="audio/wav")
    except Exception as e:
        import traceback
        print(f"[ERROR] Exception in /chat/: {e}")
        traceback.print_exc()  # 打印完整堆栈，有助排查
        return {"error": str(e)}
