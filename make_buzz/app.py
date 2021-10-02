import datetime
import json
import yaml
import boto3


def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    body = json.loads(event['body'])
    data = {
        "url": body["url"],
        "title": body["title"],
        "description": body["description"],
    }
    bucket = "devkamidata"
    
    today = datetime.date.today()
    filename = f"{today.year}/{today.month}/{today.day}/buzzcorner.yaml"

    s3obj = s3.Object(bucket,filename)
    try:
        raw_content = s3obj.get()['Body'].read().decode('utf-8')
        datas = yaml.load(raw_content)
    except s3.meta.client.exceptions.NoSuchKey:
        datas = {}
        datas['links'] = []

    datas['links'].append(data)
    content = yaml.dump(datas)
    s3obj.put(Body=bytes(content.encode('utf-8')))

    return {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": json.dumps({
            "message": "added",
        }),
    }
