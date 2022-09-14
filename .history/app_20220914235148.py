from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/room1")
def room1():
    return render_template('room1.html')

@app.route("/")
def room2():
    return render_template('room1.html')