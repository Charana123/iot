from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
def room1(name=None):
    # read data for room here from database
    return render_template('room1.html', name=name)