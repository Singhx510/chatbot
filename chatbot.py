def get_response(input_text):
    
    if "hello" in input_text.lower():
        return "Hello! How can I help you today?"
    elif "how are you" in input_text.lower():
        return "I'm just a chatbot, but thanks for asking!"
    elif "bye" in input_text.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"

def main():
    print("Chatbot: Hi! I'm a simple chatbot. You can start chatting with me or type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
