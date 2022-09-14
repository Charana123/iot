from flask import Flask, render_template
import json

app = Flask(__name__)

# get this data from a database
data = {
    'room1': [
        { 'id': 1, 'x': 300, 'y': 300, 'count': 0 },
        { 'id': 2, 'x': 800, 'y': 800, 'count': 1 },
        { 'id': 3, 'x': 300, 'y': 800, 'count': 2 },
        { 'id': 4, 'x': 800, 'y': 300, 'count': 3 },
    ],
    'room2': [
        { 'id': 1, 'x': 500, 'y': 300, 'count': 1 },
        { 'id': 2, 'x': 800, 'y': 800, 'count': 2 },
        { 'id': 3, 'x': 300, 'y': 800, 'count': 3 }
    ]
}

@app.route('/room') 
@app.route('/room/<name>')
def room(name=None):
    return render_template('room.html', data=json.dumps(data[name]))

@app.route('/update')
def update():
    # post request sends data to update database
    return