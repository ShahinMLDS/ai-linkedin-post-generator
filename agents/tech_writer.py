from utils.model import generate_text

def tech_writer(topic, language):
    prompt = f"""
Write a professional LinkedIn post about "{topic}" in {language}.

Requirements:
- 2–4 short paragraphs
- Professional tone
- Focus on technology insights
- End with a question
"""
    return generate_text(prompt)