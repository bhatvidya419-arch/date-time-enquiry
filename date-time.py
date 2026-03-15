from datetime import datetime

def chatbot():
    print("Chatbot: Hello! I can help with greetings, time, or the weather. Type 'exit' to quit.")
    
    while True:
        # Get user input and convert to lowercase for easier matching
        user_input = input("You: ").lower()

        # 1. Greetings
        if any(greet in user_input for greet in ["hi", "hello", "hey"]):
            print("Chatbot: Hello! How can I help you today?")

        # 2. Weather Inquiry
        elif "weather" in user_input:
            # Note: A real weather app would use an API like OpenWeatherMap.
            # Here, we provide a general response or local forecast data.
            print("Chatbot: Today's forecast for Bengaluru is sunny with a high of 33°C.")

        # 3. Time Inquiry
        elif "time" in user_input:
            # Using datetime module to get the current time
            now = datetime.now()
            current_time = now.strftime("%I:%M %p") # Formats to HH:MM AM/PM
            print(f"Chatbot: The current time is {current_time}.")

        # 4. Goodbye Message / Exit
        elif any(exit_cmd in user_input for exit_cmd in ["bye", "goodbye", "exit"]):
            print("Chatbot: Goodbye! Have a great day.")
            break

        else:
            print("Chatbot: I'm not sure how to respond to that. Try asking for the time or weather!")

if __name__ == "__main__":
    chatbot()
