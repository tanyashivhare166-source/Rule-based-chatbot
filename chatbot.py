# Rule Based Chatbot

print("Chatbot: Hello! I am a simple AI chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Chatbot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("Chatbot: I am fine. Thanks for asking!")

    elif "your name" in user_input:
        print("Chatbot: My name is AIBot.")

    elif "what can you do" in user_input:
        print("Chatbot: I can answer basic questions using predefined rules.")

    elif "python" in user_input:
        print("Chatbot: Python is a popular programming language used in AI and software development.")

    elif "ai" in user_input or "artificial intelligence" in user_input:
        print("Chatbot: Artificial Intelligence allows machines to think and learn.")

    elif "thank you" in user_input or "thanks" in user_input:
        print("Chatbot: You're welcome!")

    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day.")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")
