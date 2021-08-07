import os
import json
import boto3
from decimal import Decimal
        
class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)
        
def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']

    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('product')

    try:
        response = table.get_item(
            Key={
                'user': event['user']
            }
        )
        item = response['Item']
    except:
        item = 'Not found'

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(item, cls=DecimalEncoder)
    }