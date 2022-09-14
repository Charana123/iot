from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<username>')
def room1():
    return render_template('room1.html')