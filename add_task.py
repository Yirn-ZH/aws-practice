import json
import boto3
import uuid
from datetime import datetime

# Connect to DynamoDB in the correct region
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('TodoTasks')  # Make sure this matches your table name

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])  # Parses the incoming JSON from the POST request

        item = {
            'task_id': str(uuid.uuid4()),
            'title': data['title'],
            'description': data.get('description', ''),
            'status': 'pending',
            'created_at': datetime.utcnow().isoformat()
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"message": "Task added successfully!"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
