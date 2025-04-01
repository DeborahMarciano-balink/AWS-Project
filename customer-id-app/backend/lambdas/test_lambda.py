import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-north-1')
table = dynamodb.Table('customer_ids')

def lambda_handler(event, context):
    print("DEBUG - Event reçu :", json.dumps(event))  # 🔍 Ajout du debug

    if isinstance(event.get("body"), str):
        event["body"] = json.loads(event["body"])
    
    customer_id = event.get("body", {}).get("id")

    if not customer_id:
        return {"status": "error", "message": "No customer_id provided"}

    response = table.get_item(Key={'id': customer_id})

    if 'Item' in response:
        return {"exists": True}
    else:
        return {"exists": False}


if __name__ == "__main__":
    test_event = {"body": {"id": "12345"}}
    print(lambda_handler(test_event, None))
