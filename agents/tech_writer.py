from utils.model import generate_text


def tech_writer(topic, language):
    prompt = f"Write a professional LinkedIn post about {topic} in {language}. Make it 2 short paragraphs, focus on technology insights, and end with a thoughtful question."
    return generate_text(prompt)