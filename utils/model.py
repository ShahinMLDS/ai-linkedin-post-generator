from transformers import pipeline

generator = pipeline("text2text-generation", model="google/flan-t5-base")


def generate_text(prompt):
    result = generator(
        prompt,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.5
    )
    return result[0]['generated_text']