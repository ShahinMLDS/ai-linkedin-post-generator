from agents.classifier import classify_topic
from agents.tech_writer import tech_writer
from agents.general_writer import general_writer


def generate_post(topic, language):
    category = classify_topic(topic)

    print(f"\nDetected Category: {category}")

    if category == "Tech":
        return tech_writer(topic, language)
    else:
        return general_writer(topic, language)


if __name__ == "__main__":
    print("===== LinkedIn AI Agent =====")

    # Test 1
    topic1 = "AI in Healthcare"
    post1 = generate_post(topic1, "English")
    print("\n--- Output ---")
    print(post1)

    # Test 2
    topic2 = "Work-Life Balance"
    post2 = generate_post(topic2, "Bengali")
    print("\n--- Output ---")
    print(post2)