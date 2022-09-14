from flask import Flask, render_template

app = Flask(__name__)

@app.route("/room1")
def room1():
    return render_template('room1.html')