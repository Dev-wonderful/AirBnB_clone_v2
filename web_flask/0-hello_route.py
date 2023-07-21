#!/usr/bin/python3
"""Hello world using flask framework"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    """Default route"""
    return "Hello HBNB!"
