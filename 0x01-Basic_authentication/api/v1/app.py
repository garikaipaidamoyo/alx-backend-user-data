#!/usr/bin/env python3
"""
Route module for the API
"""

import sys
from os import getenv
from api.v1.auth.auth import Auth
from .views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


app = Flask(__name__)
auth = None
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

if getenv('AUTH_TYPE') == 'auth':
    auth = Auth()

def before_request():
    if auth is None:
        return

    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']

    if request.path not in excluded_paths:
        if auth.authorization_header(request) is None:
            abort(401)
        if auth.current_user(request) is None:
            abort(403)

@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
