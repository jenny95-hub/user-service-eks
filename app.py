from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample users data
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# Get all users
@app.route("/", methods=["GET"])
def get_users():
    return jsonify(users)

# Add a new user
@app.route("/", methods=["POST"])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
