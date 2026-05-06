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

    while True:
        topic = input("\nEnter a topic (or type 'exit' to quit): ")
        
        if topic.lower() == "exit":
            print("Goodbye!")
            break

        language = input("Enter language (English/Bengali): ")

        post = generate_post(topic, language)

        print("\n--- Generated Post ---")
        print(post)