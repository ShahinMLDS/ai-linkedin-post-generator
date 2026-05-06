from utils.model import generate_text

def classify_topic(topic):
    prompt = f"""
Classify the following topic into one of two categories:
Tech or General.

Topic: {topic}

Answer only one word: Tech or General.
"""
    response = generate_text(prompt)

    if "Tech" in response:
        return "Tech"
    else:
        return "General"