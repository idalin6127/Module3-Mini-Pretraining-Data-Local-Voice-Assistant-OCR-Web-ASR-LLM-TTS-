from llm import conv_manager

if __name__ == "__main__":
    test_input = "Hello, how are you?"
    print("Test input:", test_input)
    response = conv_manager.generate_response(test_input)
    print("Model response:", response)