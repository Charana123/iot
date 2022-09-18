import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('table_name')

response = table.get_item(
    Key={
        'partition_key': 'charana',
        'sort_key': 'nandasena',
    }
)
print(response['Item'])