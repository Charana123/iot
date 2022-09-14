from flask import Flask, render_template

app = Flask(__name__)

# get this data from a database
data = {
    'room1': [
        { 'id': 1, 'count': 0 },

        2: 0,
        3: 0,
        4: 0 
    ]
}

@app.route('/room/<name>')
def room(name=None):
    # read data for room here from database
    return render_template('room1.html', name=name)

@app.route('/update')
def update(name=None):
    # post request sends data to update database
    return