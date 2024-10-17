# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Math Solver Backend"

if __name__ == '__main__':
    app.run(debug=True)
