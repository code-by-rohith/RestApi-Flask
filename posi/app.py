from flask import Flask, render_template, request, jsonify
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Initialize Flask app
app = Flask(__name__)

# Ensure required NLTK resources are downloaded
nltk.download("punkt")
nltk.download("stopwords")

# Generate 10,000 responses
responses = {f"symptom_{i}": f"This is a generated response for symptom_{i}. Please consult a doctor for personalized advice." for i in range(1, 10001)}

# Function to process user input
def process_input(user_input):
    # Tokenize the input
    tokens = word_tokenize(user_input.lower())

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]

    # Match symptoms to responses
    for token in filtered_tokens:
        if token in responses:
            return responses[token]

    # Default response
    return "I'm not sure about your symptoms. Please consult a doctor for further guidance."

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    bot_response = process_input(user_input)
    return jsonify({"response": bot_response})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
