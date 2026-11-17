
import json
import random
import re
from pathlib import Path

import joblib
import numpy as np

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "intent_classifier.joblib")
vectorizer = joblib.load(BASE_DIR / "tfidf_vectorizer.joblib")

with open(BASE_DIR / "intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)

responses = {
    intent["tag"]: intent["responses"]
    for intent in data["intents"]
}

FALLBACK = (
    "Sorry, I can only help with university-related "
    "questions about admissions, fees, scholarships, "
    "and contact information."
)


def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s']", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def get_chatbot_response(message, threshold=0.30):
    cleaned = normalize_text(message)

    if not cleaned:
        return "Please enter a question."

    vector = vectorizer.transform([cleaned])

    if vector.nnz == 0:
        return FALLBACK

    probabilities = model.predict_proba(vector)[0]
    best_index = np.argmax(probabilities)

    intent = model.classes_[best_index]
    confidence = probabilities[best_index]

    if confidence < threshold:
        return FALLBACK

    return random.choice(responses.get(intent, [FALLBACK]))
