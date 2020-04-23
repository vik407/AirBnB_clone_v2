#!/usr/bin/python3
""" Write a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Add a public method def close(self)"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_id(id=None):
    """/states: display a HTML page: (inside the tag BODY)
       /states/<id>: display a HTML page: (inside the tag BODY)
    """
    state = None
    states = storage.all(State)
    if id:
        _id = "State." + id
        if _id in states.keys():
            state = states[_id]
    return render_template('9-states.html', **locals())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
