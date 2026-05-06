from utils.model import generate_text


def classify_topic(topic):
    prompt = f"Classify the topic '{topic}' as Tech or General. Answer only with 'Tech' or 'General'."
    response = generate_text(prompt)

    if "Tech" in response:
        return "Tech"
    else:
        return "General"