import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('customer_ids')

def lambda_handler(event, context):
    try:
        body = event.get('body')
        if not body:
            raise ValueError("Request body is missing.")

        data = json.loads(body)

        if 'id' not in data:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': "ID is missing in the request body."})
            }

        customer_id = data['id']

        # Insert the customer ID into the DynamoDB table
        table.put_item(Item=data)

        return {
            'statusCode': 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",  
                "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization"
            },
            'body': json.dumps({'message': "Client updated successfully.", 'id': customer_id})
        }

    except ValueError as ve:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': str(ve)})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': "Error occurred while updating the client.", 'error': str(e)})
        }
