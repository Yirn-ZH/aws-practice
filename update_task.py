# 3️⃣ Lambda Function: Update Task
# File: lambdas/update_task.py
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTasks')

def lambda_handler(event, context):
    task_id = event['pathParameters']['task_id']
    data = json.loads(event['body'])

    update_expr = 'SET ' + ', '.join(f"{k}=:{k}" for k in data.keys())
    expr_values = {f":{k}": v for k, v in data.items()}

    table.update_item(
        Key={'task_id': task_id},
        UpdateExpression=update_expr,
        ExpressionAttributeValues=expr_values
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Task updated successfully!'})
    }