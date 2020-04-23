#!/usr/bin/python3
""" Write a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Add a public method def close(self)"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """/hbnb: display a HTML page like 8-index.html, done during the
    0x01. AirBnB clone - Web static project"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    table = {}
    for p, u in storage._DBStorage__session.query(Place, User).\
            filter(Place.user_id == User.id):
        table[p.user_id] = "{} {}".format(u.first_name, u.last_name)
    return render_template('100-hbnb.html', **locals())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
