import json
import boto3
import uuid
import time
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CalculatorResult')

def lambda_handler(event, context):
    
    if 'body' in event:
        body = json.loads(event['body'])
    else:
        body = event

    num1 = Decimal(body['num1'])
    num2 = Decimal(body['num2'])
    operation = body['operation']

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2

    item = {
        "id": str(uuid.uuid4()),
        "num1": num1,
        "num2": num2,
        "operation": operation,
        "result": result,
        "timestamp": str(time.time())
    }

    table.put_item(Item=item)

    return {
    "statusCode": 200,
    "headers": {"Access-Control-Allow-Origin": "*"},
    "result": float(result)   # return directly
}
