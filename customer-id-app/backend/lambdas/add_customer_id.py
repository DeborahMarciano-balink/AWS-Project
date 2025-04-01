import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-north-1')
table = dynamodb.Table('customer_ids')

def lambda_handler(event, context):
    customer_id = event.get('customer_id')

    if not customer_id:
        return {"status": "error", "message": "No customer_id provided"}

    table.put_item(Item={'id': customer_id})
    
    return {"status": "success", "message": "Customer ID added successfully"}
    
if __name__ == "__main__":
    test_event = {"customer_id": "67890"}
    print(lambda_handler(test_event, None))
