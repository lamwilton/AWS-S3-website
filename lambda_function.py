from datetime import datetime

def lambda_handler(event, context):
    
    time = datetime.now().strftime("%B %d,%Y %H:%M:%S")

    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": str(event['headers']['X-Forwarded-For']) + " Current time: " + str(time) + " GMT"
    }

    return resp