import os
import json
import random
        
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Eligible": bool(random.getrandbits(1))
        })
    }