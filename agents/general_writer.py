def general_writer(topic, language):
    prompt = f"""
Write a LinkedIn post.

Topic: {topic}
Language: {language}

Rules:
- Write ONLY the post
- 2 short paragraphs
- Simple and engaging
- No repetition
- End with a question
"""
    return generate_text(prompt)