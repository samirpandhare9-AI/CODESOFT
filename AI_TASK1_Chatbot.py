# TASK 1: Rule-Based Chatbot

# 1. Set the rules (questions and answers)
rules = {
    "hello": "Hi there! I am an AI assistant. How can I help you today?",
    "how are you": "I am a program, but I am functioning well! How about you?",
    "name": "I don't have a name, I am just a simple program.",
    "bye": "Goodbye! Have a nice day.",
    "thank you": "You're welcome!",
}# 2. Function that generates the response
def get_response(user_input):
    # Convert input to lowercase for easier comparison
    user_input = user_input.lower()  
    
    # Check if any keyword in our rules matches the user input
    for word in rules:
        if word in user_input:
            return rules[word]  # Return the correct response
    
    # If no match is found, return a default message
    return "I am sorry, I do not understand that. Try asking about 'hello' or 'name'."

# 3. Main Chat Loop (The part that runs the program)
print("ChatBot: Hello! Type your message to start. (Type 'bye' to stop)")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "bye":
        print("ChatBot: Goodbye! Thank you for chatting.")
        break  # Exit the loop
        
    response = get_response(user_input)
    print(f"ChatBot: {response}")

# End of code