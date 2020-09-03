#!/usr/bin/python3
"""Write a script that starts a Flask web application
and would be listening on 0.0.0.0, port 5000"""
from flask import Flask, request, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    """/states folder with an id

    Returns:
        [HTML content: [display a HTML page: (inside the tag BODY)]
    """
    states = storage.all(State)
    if id is None:
        return render_template("9-states.html", states=states)
    else:
        return render_template(
            "9-states.html", states=states, id="State." + id)


@app.teardown_appcontext
def remove_session(exception):
    """fter each request you must remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
