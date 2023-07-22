#!/usr/bin/python3
"""Hello world using flask framework"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Default route"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb route"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """c route"""
    text = text.replace('_', ' ')
    return "c {}".format(text)


if __name__ == '__main__':
    app.run('localhost', debug=True)
