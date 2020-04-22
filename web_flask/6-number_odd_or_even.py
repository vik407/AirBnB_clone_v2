#!/usr/bin/python3
""" Write a script that starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """/: display “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """/hbnb: display “HBNB”"""
    return 'HBNB'


@app.route('/c/<var>', strict_slashes=False)
def c(var):
    """/c/<text>: display “C ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    return 'C %s' % var.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """/python/(<text>): display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>')
def num(n):
    """/number/<n>: display “n is a number” only if n is an integer"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def num_template(n):
    """/number_template/<n>: display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """/number_odd_or_even/<n>: display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
