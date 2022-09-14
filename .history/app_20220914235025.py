from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def room1():
    return render_template('room1.html')

def hello():
    return render_template('room1.html')