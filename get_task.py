import json

# 2️⃣ Lambda Function: Get Tasks
# File: lambdas/get_tasks.py
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTasks')

def lambda_handler(event, context):
    response = table.scan()
    tasks = response.get('Items', [])

    return {
        'statusCode': 200,
        'body': json.dumps(tasks)
    }
