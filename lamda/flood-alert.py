# Lambda code will go here
#Purpose
1
-Test AWS Lambda
-Check if Lambda is working
def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": "Terai Flood Alert System Running"
    }

2
-First flood logic
-Introduced Safe / Warning / Danger
def lambda_handler(event, context):

    RiverName = "Bheri"
    WaterLevel = 9

    if WaterLevel >= 9:
        Status = "Danger"

    elif WaterLevel >= 7:
        Status = "Warning"

    else:
        Status = "Safe"

    return {
        "statusCode": 200,
        "body": f"River: {RiverName} | Level: {WaterLevel}m | Status: {Status}"
    }
  3
-River: Bheri | Level: 5m | Status: Safe
def lambda_handler(event, context):

    RiverName = "Bheri"
    WaterLevel = 5

    if WaterLevel >= 9:
        Status = "Danger"

    elif WaterLevel >= 7:
        Status = "Warning"

    else:
        Status = "Safe"

    return {
        "statusCode": 200,
        "body": f"River: {RiverName} | Level: {WaterLevel}m | Status: {Status}"
    }
  4
-Reads data from DynamoDB
-No hardcoded water level
import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):

    table = dynamodb.Table('RiverLevels')

    response = table.get_item(
        Key={
            'RiverName': 'Bheri'
        }
    )

    item = response['Item']

    RiverName = item['RiverName']
    WaterLevel = int(item['WaterLevel'])

    if WaterLevel >= 9:
        Status = "Danger"

    elif WaterLevel >= 7:
        Status = "Warning"

    else:
        Status = "Safe"

    return {
        "statusCode": 200,
        "body": f"River: {RiverName} | Level: {WaterLevel}m | Status: {Status}"
    }

