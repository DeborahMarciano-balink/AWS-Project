import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='eu-north-1')
table = dynamodb.Table('customer_ids')

def lambda_handler(event, context):
    try:
        print(f"Received event: {json.dumps(event)}")

        if isinstance(event.get("body"), str):
            event["body"] = json.loads(event["body"])

    
        customer_id = event.get("body", {}).get("id")
        print(f"Customer ID: {customer_id}")

        if not customer_id:
            print("No customer_id provided")
            return {"status": "error", "message": "No customer_id provided"}

        
        response = table.get_item(Key={'id': customer_id})
        print(f"Response from DynamoDB: {json.dumps(response)}")

        if 'Item' in response:
            print("Customer ID exists")
            return {"exists": True}
        else:
            print("Customer ID does not exist")
            return {"exists": False}

    except Exception as e:
        print(f"Error: {str(e)}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    test_event = {"body": {"id": "12345"}}
    print(lambda_handler(test_event, None))
