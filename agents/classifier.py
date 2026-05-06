def classify_topic(topic):
    prompt = f"""
Classify this topic as Tech or General.

Topic: {topic}

Answer:
"""
    response = generate_text(prompt)

    if "Tech" in response:
        return "Tech"
    else:
        return "General"