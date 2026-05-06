def tech_writer(topic, language):
    prompt = f"""
Write a LinkedIn post.

Topic: {topic}
Language: {language}

Rules:
- Write ONLY the final post
- 2 short paragraphs
- Professional tone
- No repetition
- No explanation
- End with a question
"""
    return generate_text(prompt)