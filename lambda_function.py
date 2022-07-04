import json
import boto3
import base64
s3 = boto3.client('s3')

def lambda_handler(event, context):
    print(event)
    if event['httpMethod'] == 'POST': 
        print(event['body'])
        data = json.loads(event['body'])
        name = data['name']
        image = data['file']
        image = image[image.find(",")+1:]
        dec = base64.b64decode(image + "===")
        
        s3.put_object(Bucket='ngp-image-container-bucket-01', Key=name, Body=dec)
        
        return {'statusCode': 200, 
        'body': "successful lambda function call"}