import boto3

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

TOPIC_ARN = "arn:aws:sns:ap-northeast-3:932333195607:FloodAlertTopic"

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

        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject='Flood Alert',
            Message=f'Flood Alert!\n\nRiver: {RiverName}\nWater Level: {WaterLevel}m\nStatus: Danger'
        )

    elif WaterLevel >= 7:
        Status = "Warning"

    else:
        Status = "Safe"

    return {
        "statusCode": 200,
        "body": f"River: {RiverName} | Level: {WaterLevel}m | Status: {Status}"
    }
