import boto3

dynamodb = boto3.resource('dynamodb')

rooms = dynamodb.Table('rooms').scan()['Items']

print(rooms)