#!/usr/bin/python3
"""flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """list all states"""
    states = storage.all(State).values()
    # print(states)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def end_session(error=None):
    """close the session"""
    storage.close()


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
