from datetime import datetime
import boto3

def writeDB(time, ip, origin):
    db = boto3.client('dynamodb')
    db.put_item(TableName='myWebsiteTable', Item={'time' :{'S': time}, 'ip' : {'S': ip}, 'origin' : {'S': origin}})


def lambda_handler(event, context):
    timeLong = datetime.now().strftime("%B %d, %Y %H:%M:%S")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = event['headers']['X-Forwarded-For']
    origin = event['headers']['origin']
    
    if ip != "128.125.146.206": # Not writing database for  myself
        writeDB(time, ip, origin)
    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": str(ip) + " Current time: " + str(timeLong) + " GMT"
    }
    
    return resp