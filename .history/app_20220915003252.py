from flask import Flask, render_template

app = Flask(__name__)

@app.route('/room/<name>')
def room(name=None):
    # read data for room here from database
    return render_template('room1.html', name=name)

@app.route('/update')
def update(name=None):
    # post request sends data to update database
    return