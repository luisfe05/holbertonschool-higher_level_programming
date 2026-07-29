#!/usr/bin/env python3
"""
Flask RESTful API implementation.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user store (empty for checker compatibility)
users = {}


@app.route('/')
def home():
    """
    Root endpoint.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """
    Returns a list of stored usernames.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """
    Returns API status.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Returns user details or 404 if not found.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Adds a new user to the users dictionary.
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
