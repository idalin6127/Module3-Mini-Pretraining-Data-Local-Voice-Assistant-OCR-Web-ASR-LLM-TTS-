# from transformers import pipeline, Conversation, AutoTokenizer

# model_name = "microsoft/DialoGPT-small"
# tokenizer = AutoTokenizer.from_pretrained(model_name)


# tokenizer.padding_side = "left"
# if tokenizer.pad_token is None:
#     tokenizer.pad_token = tokenizer.eos_token

# # 创建pipeline，指定tokenizer
# conv_pipeline = pipeline("conversational", model=model_name, tokenizer=tokenizer)

# class ConversationManager:
#     def __init__(self):
#         self.conversation = Conversation()  # 初始化一个空对话

#     def generate_response(self, user_text):
#         # 把用户输入添加到对话中
#         self.conversation.add_user_input(user_text)
#         # 用Conversation对象调用pipeline
#         result = conv_pipeline(self.conversation)
#         bot_response = result.generated_responses[-1]
#         print(f"[User]: {user_text}")
#         print(f"[Bot]: {bot_response}")
#         return bot_response

# conv_manager = ConversationManager()

# if __name__ == "__main__":
#     cm = ConversationManager()
#     test_text = "Hello, how are you?"
#     response = cm.generate_response(test_text)
#     print(f"Model response: {response}")
# 。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。


# from transformers import pipeline, AutoTokenizer, Conversation

# class ConversationManager:
#     def __init__(self):
#         model_name = "microsoft/DialoGPT-small"
#         self.tokenizer = AutoTokenizer.from_pretrained(model_name)
#         # 关键：设置padding_side为left，且如果pad_token没设置就设为eos_token
#         self.tokenizer.padding_side = "left"
#         if self.tokenizer.pad_token is None:
#             self.tokenizer.pad_token = self.tokenizer.eos_token

#         self.conv_pipeline = pipeline(
#             "conversational",
#             model=model_name,
#             tokenizer=self.tokenizer,
#             pad_token_id=self.tokenizer.eos_token_id,
#         )
#         self.conversation = Conversation()

#     def generate_response(self, user_text):
#         self.conversation.add_user_input(user_text)
#         result = self.conv_pipeline(self.conversation, max_length=100, do_sample=True, top_k=50, top_p=0.95, temperature=0.7)
#         bot_response = result.generated_responses[-1]
#         print(f"[User]: {user_text}")
#         print(f"[Bot]: {bot_response}")
#         return bot_response


# if __name__ == "__main__":
#     cm = ConversationManager()
#     response = cm.generate_response("Hello, how are you?")
#     print(f"Model response: {response}")

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, Conversation

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small", padding_side="left")

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small", pad_token_id=tokenizer.eos_token_id)

conv_pipeline = pipeline("conversational", model=model, tokenizer=tokenizer)

conv_pipeline.tokenizer.pad_token = tokenizer.pad_token

# 使用更现代的generation config方式(如果需要自定义)
from transformers import GenerationConfig
generation_config = GenerationConfig(
    pad_token_id=tokenizer.pad_token_id,
    eos_token_id=tokenizer.eos_token_id,
    pad_token=tokenizer.pad_token,
)

class ConversationManager:
    def __init__(self):
        self.conversation = Conversation()

    def generate_response(self, user_text):
        self.conversation.add_user_input(user_text)
        # 这里传入generation config参数减少警告
        result = conv_pipeline(self.conversation, generation_config=generation_config)
        bot_response = result.generated_responses[-1]
        print(f"[User]: {user_text}")
        print(f"[Bot]: {bot_response}")
        return bot_response

conv_manager = ConversationManager()

if __name__ == "__main__":
    cm = ConversationManager()
    test_text = "Hello, how are you?"
    response = cm.generate_response(test_text)
    print(f"Model response: {response}")


