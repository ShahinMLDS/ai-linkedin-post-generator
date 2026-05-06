from utils.model import generate_text


def general_writer(topic, language):
    prompt = f"Write an engaging LinkedIn post about {topic} in {language}. Make it 2 short paragraphs, suitable for a general audience, and end with a thoughtful question."
    return generate_text(prompt)