from flask import Flask
"""
Flask web application listening on 0.0.0.0, port 5000
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the
text variable (replace underscore _
"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    method that returns arg passed
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    method that returns arg passed
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
"""
 this route definition uses the defaults keyword argument
 to specify a default value of "is cool"
"""


@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
