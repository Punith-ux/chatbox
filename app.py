from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")

def home():
    return "Chatbot API Running"

@app.route("/chat", methods=["POST"])

def chat():
    data = request.json

    message = data.get("message")

    response = "I received: " + message

    return jsonify({
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)