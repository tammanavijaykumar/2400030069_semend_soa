
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "User Service is running!"
    })

@app.route("/users")
def get_users():
    return jsonify({
        "service": "User Service",
        "user_id": 101,
        "name": "Naren"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
