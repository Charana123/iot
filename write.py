import boto3
import time
import datetime
import random

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('occupancy')

ts = time.time()
ts = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

table.put_item(
   Item={
        'room_name': 'room1',
        'timestamp': ts,
        'count': random.randint(0, 10)
    }
)