import json
import random
import string

# Load intents from JSON file
with open("intents.json") as file:
    data = json.load(file)

# Text preprocessing function
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = text.split()
    return tokens

# Find best matching intent
def get_response(user_input):
    tokens = preprocess(user_input)

    best_intent = None
    max_score = 0

    # Loop through intents
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern_tokens = preprocess(pattern)
            score = 0

            # Count matching words
            for word in tokens:
                if word in pattern_tokens:
                    score += 1

            # Select intent with highest match score
            if score > max_score:
                max_score = score
                best_intent = intent

    # Return response
    if best_intent:
        return random.choice(best_intent["responses"])
    else:
        return "Sorry, I didn't understand that."

# Chat loop
print("Chatbot is running! Type 'exit' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = get_response(user_input)
    print("Bot:", response)
