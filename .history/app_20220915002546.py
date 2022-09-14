from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<name>')
def room1(name=None):
    return render_template('room1.html', name=name)