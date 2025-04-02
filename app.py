from flask import Flask, request, jsonify, send_from_directory
import os
from flask_cors import CORS

app = Flask(__name__, static_folder="static", static_url_path="/")

# API Route (Chatbot)
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    response = f"You said: {user_message}"
    return jsonify({"response": response})

# Serve Frontend Files (index.html)
@app.route("/")
def serve_frontend():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
