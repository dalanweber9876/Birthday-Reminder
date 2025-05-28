import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

def generate_message_custom(name, background):
    print("Hit")
    # Load tokenizer and model
    MODEL_NAME = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token

    model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)
    model.resize_token_embeddings(len(tokenizer))
    model.load_state_dict(torch.load("apps/ai_messages/model/model.pth", map_location=torch.device("cpu")))
    model.eval()

    # Get user input
    # name = input("Enter a name: ")
    tone = 'heartfelt'
    # background = input("Enter some background:\n")

    # Prepare input
    prompt = (
        f"You are an AI that writes birthday messages.\n"
        f"The tone of the message should be {tone}.\n"
        f"Name: {name}\n"
        f"Background: {background}\n"
        f"Message:"
    )

    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=128)
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]

    # Generate
    with torch.no_grad():
        output_ids = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=150,
            temperature=0.8,
            top_k=50,
            top_p=0.95,
            do_sample=True,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.eos_token_id
        )

    message = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    generated_message = message[len(prompt):].strip()
    print("🎉 Generated Birthday Message:\n")
    print(generated_message)
    return generated_message
