from flask import Flask, render_template
import boto3
import json

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb')
rooms = dynamodb.Table('rooms').scan['Items']

@app.route('/') 
def index():
    return render_template('room.html', data=json.dumps(rooms))

@app.route('/') 
def index():
    return render_template('room.html', data=json.dumps(rooms))

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)