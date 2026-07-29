#!/usr/bin/env python3
"""
API Security module implementing Basic Auth, JWT Auth, and Role-Based Access.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
    JWTManager,
)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Configure Secret Key for JWT Token Generation
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-this"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory user database
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


# --- Basic Auth Verification ---
@auth.verify_password
def verify_password(username, password):
    """
    Verifies user credentials for Basic Authentication.
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


# --- Custom JWT Error Handlers (Ensures 401 status code) ---
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handles missing or invalid token error."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handles invalid token error."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handles expired token error."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handles revoked token error."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handles needs fresh token error."""
    return jsonify({"error": "Fresh token required"}), 401


# --- API Routes ---
@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Protected route requiring Basic HTTP Authentication.
    """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Authenticates user and returns a JWT token with user role embedded.
    """
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    username = request.json.get("username")
    password = request.json.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    additional_claims = {"role": user["role"]}
    access_token = create_access_token(
        identity=username,
        additional_claims=additional_claims
    )
    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Protected route requiring a valid JWT Token.
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Protected route requiring JWT with admin role.
    """
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
