#!/usr/bin/python3
"""Write a script that starts a Flask web application
and would be listening on 0.0.0.0, port 5000"""
from flask import Flask, request, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filter():
    """/states folder with an id

    Returns:
        [HTML content: [display a HTML page: (inside the tag BODY)]
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template(
        "10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def remove_session(exception):
    """fter each request you must remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
