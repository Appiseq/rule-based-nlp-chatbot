
# Rule-Based NLP Chatbot

## Overview
A simple rule-based chatbot built using Python that interprets user input
by matching it with predefined intents stored in a JSON file.

## Technologies Used
- Python
- NumPy
- JSON

## How It Works
1. User input is preprocessed (lowercasing, tokenization).
2. Input tokens are compared with intent patterns from a JSON file.
3. The intent with the highest match score is selected.
4. A dynamic response is returned.

## Limitations
- Cannot handle unseen intents.
- Rule-based matching may fail for complex queries.

## Future Improvements
- Replace rule-based logic with ML/DL-based intent classification.

## Features
- Preprocesses user text (lowercasing, punctuation removal)
- Matches user input to intent patterns
- Selects best intent based on simple keyword scoring
- Returns random dynamic response from matched intent


## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Appiseq/rule-based-nlp-chatbot.git
   cd rule-based-nlp-chatbot
   python chatbot.py

   
## Contributing

Feel free to open issues or submit pull requests for improvements!






