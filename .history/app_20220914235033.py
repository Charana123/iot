from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def room1():
    return render_template('room1.html')

def room2():
    return render_template('room1.html')