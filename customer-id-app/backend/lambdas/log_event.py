import json

def lambda_handler(event, context):

    print(f"Event logged: {json.dumps(event)}")

    return {"status": "success", "message": "Event logged successfully"}
    
if __name__ == "__main__":
    test_event = {"customer_id": "12345", "event": "Existing ID"}
    print(lambda_handler(test_event, None))
