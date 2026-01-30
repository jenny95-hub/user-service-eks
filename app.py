from flask import Flask, jsonify, request
import logging
import sys

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.route("/", methods=["GET"])
def get_users():
    app.logger.info("GET / called")
    return jsonify(users)

@app.route("/", methods=["POST"])
def add_user():
    new_user = request.get_json()
    app.logger.info(f"POST / called with payload: {new_user}")
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
