#!/usr/bin/python3
"""Hello world using flask framework"""
from flask import Flask
from markupsafe import escape

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
    return "C {}".format(escape(text))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is_cool"):
    """python route"""
    text = text.replace('_', ' ')
    return "Python {}".format(escape(text))


if __name__ == '__main__':
    app.run('localhost', debug=True)
