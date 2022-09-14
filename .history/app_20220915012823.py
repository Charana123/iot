from flask import Flask, render_template

app = Flask(__name__)

# get this data from a database
data = {
    'room1': [
        { 'id': 1, 'count': 0 },
        { 'id': 2, 'count': 0 },
        { 'id': 3, 'count': 0 },
        { 'id': 4, 'count': 0 },
    ],
    'room2': [
        { 'id': 1, 'count': 0 },
        { 'id': 2, 'count': 0 },
        { 'id': 3, 'count': 0 },
        { 'id': 4, 'count': 0 },
    ]
}

@app.route('/room')
@app.route('/room/<name>')
def room(name=None):
    # read data for room here from database
    print(data[name])
    return render_template('room.html', name=name, data=data[name])

@app.route('/update')
def update(name=None):
    # post request sends data to update database
    return