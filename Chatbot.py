def chatbot():
    print("ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("ChatBot: Hi! How can I help you?")

        elif "name" in user:
            print("ChatBot: My name is CodSoft Bot.")

        elif "how are you" in user:
            print("ChatBot: I am fine. Thank you!")

        elif "course" in user:
            print("ChatBot: I can help you with AI and Python related queries.")

        elif user == "bye":
            print("ChatBot: Goodbye! Have a nice day.")
            break

        else:
            print("ChatBot: Sorry, I don't understand that.")

chatbot()
