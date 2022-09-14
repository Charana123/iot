from flask import Flask, url_for
from flask import render_template

app = Flask(__name__)
url_for('static', filename='style.css')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)