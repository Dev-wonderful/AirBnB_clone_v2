#!/usr/bin/python3
"""Hello world using flask framework"""
from flask import Flask, render_template
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


@app.route("/number/<int:n>")
def number_route(n):
    """Number route"""
    return "{} is a number".format(escape(n))


@app.route("/number_template/<int:n>")
def number_template(n):
    """Display template if route is a number"""
    return render_template("5-number.html", number=n)


if __name__ == '__main__':
    app.run('localhost', debug=True)
