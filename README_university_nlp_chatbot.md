# University NLP Chatbot 🎓

An intent-based university student support chatbot built with **Python, scikit-learn, TF-IDF, Logistic Regression, and Streamlit**. It classifies student questions into six supported intents and returns predefined responses from a JSON knowledge base.

> **Project status:** Working local prototype. Responses are informational placeholders, not verified university policies. The chatbot is not an LLM or generative AI system.

## Features

- Interactive chat interface built with Streamlit
- Six supported intents: greetings, admissions, fees, scholarships, contact information, and goodbye
- Text normalization and TF-IDF features (unigrams and bigrams)
- Logistic Regression intent classification
- Basic fallback handling for low-probability or unknown-vocabulary messages
- Session-based chat history in the UI
- Predefined, editable responses in `intents.json`

## Tech stack

- Python
- Streamlit
- scikit-learn
- NumPy
- Joblib
- JSON

## Project structure

```text
university-nlp-chatbot/
├── app.py
├── chatbot.py
├── intents.json
├── intent_classifier.joblib
├── tfidf_vectorizer.joblib
├── requirements.txt
├── README.md
└── .gitignore
```

## How it works

```text
Student message
    ↓
Text normalization
    ↓
TF-IDF vectorization
    ↓
Logistic Regression intent prediction
    ↓
Vocabulary and probability-based fallback checks
    ↓
Predefined response from intents.json (or fallback)
```

The model predicts an intent rather than generating new answers. A basic probability threshold of **0.30** is used as a provisional fallback rule; it has not been calibrated for production use.

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/university-nlp-chatbot.git
cd university-nlp-chatbot
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment (optional but recommended)

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. Start the app

**Windows PowerShell:**

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Or, if using your existing Python environment:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL shown in your terminal (usually `http://localhost:8501`).

**Important:** The two `.joblib` files are required to run the app. Only load model files from trusted sources.

## Example questions

| Student message | Expected intent |
| --- | --- |
| Hello there | `greeting` |
| How can I get admission? | `admission_query` |
| What is the semester fee? | `fee_query` |
| Are scholarships available? | `scholarship_query` |
| How do I contact the university? | `contact_query` |
| Goodbye | `goodbye` |

Out-of-domain requests, such as booking a flight, should trigger a fallback, but the current approach is not guaranteed to reject every unsupported question.

## Evaluation

The initial intent classifier was evaluated on a held-out set of **30 messages** (five per intent):

| Metric | Result |
| --- | ---: |
| Accuracy | **73.33%** (22/30) |
| Macro precision | 0.75 |
| Macro recall | 0.73 |
| Macro F1-score | 0.73 |

A separate **18-message diagnostic check** with a provisional 0.30 threshold yielded **88.89%** (16/18), including rejection of six out-of-scope examples. This small diagnostic check is **not** an independent benchmark and should not be compared directly with the held-out classification accuracy.

### Known limitations

- Small, manually constructed dataset; generalization is limited
- Some valid messages are rejected by the fallback threshold
- Out-of-scope detection relies on vocabulary overlap and classifier probabilities
- No multi-turn intent understanding or conversational context tracking
- Responses are generic placeholders and should be verified before use by a real institution
- Model probability estimates are not calibrated confidence scores

## Future improvements

- Collect more diverse, independently labeled examples
- Add a dedicated out-of-scope class and a separate validation dataset
- Evaluate precision/recall for fallback decisions
- Improve classification of payment-plan and student-support questions
- Add tests and pin tested dependency versions
- Deploy the Streamlit application and include its live URL here

## Author

**Gotam Kumar**  
BS Artificial Intelligence student  
GitHub: [eng-gotam](https://github.com/eng-gotam)

## Disclaimer

This is an educational machine-learning project. It is not affiliated with or endorsed by a university. Always consult official university sources for current admissions, fees, scholarships, and contact details.
