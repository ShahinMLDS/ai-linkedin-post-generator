from utils.model import generate_text

def general_writer(topic, language):
    prompt = f"""
Write a professional LinkedIn post about "{topic}" in {language}.

Requirements:
- 2–4 short paragraphs
- Professional tone
- Suitable for general audience
- End with a question
"""
    return generate_text(prompt)