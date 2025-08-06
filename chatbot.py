def chatbot():
    print("Chatbot: Hello!  (type 'bye' to exit).")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print(" Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print(" Chatbot: Goodbye!")
        elif user_input == "can u help me":
            print(" Chatbot:  sure!tell me your problem")
        elif user_input == "can u sing a song":
            print(" Chatbot:  Sorry but i am only text based Ai")
            break
        else:
            print(" Chatbot: Sorry, I don't understand.")

# Run the chatbot
chatbot()
