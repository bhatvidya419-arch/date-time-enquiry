def respond_to_emotion(user_input):
    user_input = user_input.lower()
    
    if "i am sad" in user_input:
        return "I'm sorry to hear that. I'm here if you want to chat or hear a joke!"
    elif "i am happy" in user_input:
        return "That's wonderful! Your positive energy is contagious."
    else:
        return "I see. How are you feeling overall?"

# Test
print(respond_to_emotion("I am sad"))
