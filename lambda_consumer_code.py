import base64
import boto3
import json



def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    bucket_name = 'stock.data.kinesis'  # Replace with your S3 bucket name

    # Iterate over each record from the Kinesis Data Stream
    for record in event['Records']:
        # Decode the base64-encoded data
        payload = base64.b64decode(record['kinesis']['data'])
        data = json.loads(payload)
        print(data)
        
        # Convert the data to a string
        data_str = json.dumps(data)
        
        # Generate a unique S3 object key
        object_key = f"{data['Index']}_{data['Date']}.json"
        
        # Upload the data to S3
        s3_client.put_object(
            Bucket=bucket_name,
            Key=object_key,
            Body=data_str
        )

    return {
        'statusCode': 200,
        'body': 'Data loaded into S3'
    }
        


