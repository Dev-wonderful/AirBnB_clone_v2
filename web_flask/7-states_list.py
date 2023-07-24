#!/usr/bin/python3
"""flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """list all states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def end_session():
    """close the session"""
    storage.close()


if __name__ == '__main__':
    app.run('localhost', debug=True)
