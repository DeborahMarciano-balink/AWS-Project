import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-north-1')
table = dynamodb.Table('customer_ids')

def lambda_handler(event, context):
    customer_id = event.get('customer_id')

    if not customer_id:
        return {"status": "error", "message": "No customer_id provided"}

    response = table.get_item(Key={'id': customer_id})

    if 'Item' in response:
        return {"exists": True}
    else:
        return {"exists": False}
    
if __name__ == "__main__":
    test_event = {"customer_id": "12345"}
    print(lambda_handler(test_event, None))



