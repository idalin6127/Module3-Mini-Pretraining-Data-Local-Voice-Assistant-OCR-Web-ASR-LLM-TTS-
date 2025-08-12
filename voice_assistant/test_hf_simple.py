from transformers import pipeline

def test_generation():
    generator = pipeline("text-generation", model="distilgpt2", pad_token_id=50256)
    input_text = "Hello, how are you?"
    output = generator(input_text, max_new_tokens=50)
    print("Generated text:", output[0]['generated_text'])

if __name__ == "__main__":
    test_generation()
