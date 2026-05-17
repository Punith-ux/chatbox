import json
import random
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents
with open("intents.json") as file:
    data = json.load(file)

texts = []
labels = []

# Prepare dataset
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        texts.append(pattern)
        labels.append(intent["tag"])

# Vectorize text
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression()

model.fit(X, labels)

# Chat loop
print("Chatbot is running! Type 'quit' to stop.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    user_vector = vectorizer.transform([user_input])

    prediction = model.predict(user_vector)[0]

    for intent in data["intents"]:
        if intent["tag"] == prediction:
            response = random.choice(intent["responses"])
            print("Bot:", response)