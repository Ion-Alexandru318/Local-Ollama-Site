from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/generate"  # To Ollama API. Original URL meant for a other device to VM

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Please enter a message."}), 400

    payload = {
        "model": "llama3",
        "prompt": user_message,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        ai_reply = response.json().get("response", "No response from model.")
        return jsonify({"reply": ai_reply})
    except requests.exceptions.RequestException as e:
        return jsonify({"reply": f"Error connecting to Ollama: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=9901)