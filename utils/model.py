from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Use FLAN-T5 (better than GPT-2)
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def generate_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(**inputs, max_length=200, do_sample=False)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)