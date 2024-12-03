import string
import os
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "microsoft/DialoGPT-large"

def NLPModel(prompt):
    global model_name
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    inputs = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors="pt")

    outputs = model.generate(inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Remove the prompt from the response
    response = response[len(prompt):].strip()

    if response.strip() == "":
        response = "I'm sorry, I didn't catch that."

    os.system('cls')
    return response
