#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"

users = {}

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return jsonify({"status": "OK"})

@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    return jsonify({
        "messge": "User added successfully",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run()
