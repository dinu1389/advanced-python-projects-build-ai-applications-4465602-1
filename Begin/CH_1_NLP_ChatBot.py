from textblob import TextBlob

intents = {
    "greeting": ["hello", "hi", "hey"],
    "farewell": ["bye", "goodbye", "see you"],
    "thanks": ["thank you", "thanks"],
    "help": ["help", "assist", "support"],
    "hours": {
        "keywords": ["hours", "open", "close"],
        "response": "Our store is open from 9 AM to 9 PM every day."
    },
    "return": {
        "keywords": ["return", "refund", "exchange"],
        "response": "You can return items within 30 days of purchase with a receipt."
    }
}

def get_response(message):
    message = message.lower()  # Convert the message to lowercase for consistent keyword matching
    
    for intent, data in intents.items():
        if isinstance(data, dict):  # Check if the intent has a dictionary of keywords and response
            keywords = data["keywords"]
            response = data["response"]
            if any(keyword in message for keyword in keywords):
                return response
        else:  # If the intent is a list of keywords
            if any(keyword in message for keyword in data):
                return f"{intent.capitalize()} detected. How can I assist you?"
    
    # Analyze the sentiment of the message using TextBlob
    sentiment = TextBlob(message).sentiment.polarity
    
    if sentiment > 0:
        return "I'm glad to hear that! How can I assist you further?"
    elif sentiment < 0:
        return "I'm sorry to hear that. Is there anything I can do to help?"
    else:
        return "Thank you for sharing. How can I assist you today?"

# Define intents and their corresponding responses based on keywords

    # Convert the message to lowercase for consistent keyword matching
  
    # Check if the message contains any keywords associated with defined intents
    
    
    # Analyze the sentiment of the message using TextBlob

    
    # Return a response based on the sentiment score
   
    # Greet the user and prompt for input
   
    # Continuously prompt the user for input until they choose to exit
   
    # Thank the user for chatting when they exit
def chat():
    print("Welcome to the chatbot! Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Chatbot: Thank you for chatting! Goodbye!")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()  # Start the chat when the script is executed
