#!/usr/bin/python3
"""Write a script that starts a Flask web application
and would be listening on 0.0.0.0, port 5000"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def function():
    """main or home route

    Rules that end with a slash are “branches”, others
    are “leaves”. If << strict_slashes >> is enabled
    (the default), visiting a branch URL without a
    trailing slash will redirect to the URL with a slash appended.

    Returns:
            [string]: [display “Hello HBNB!”]
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
