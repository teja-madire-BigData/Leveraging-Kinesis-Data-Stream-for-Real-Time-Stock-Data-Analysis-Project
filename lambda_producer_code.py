import pandas as pd
import boto3
import base64
import json
import time

def lambda_handler(event, context):
    # Define your Kinesis Data Stream details
    stream_name = 'stock_market_streaming_realtime'
    region_name = 'ap-south-1'

    # Read the CSV file using pandas
    df = pd.read_csv('stock_data.csv')

    # Convert the DataFrame to JSON records
    records = df.to_dict(orient='records')

    # Initialize the Kinesis client
    kinesis = boto3.client('kinesis', region_name=region_name)

    # Send each record to the Kinesis Data Stream with a delay
    for record in records:
        # Convert the record to a JSON string
        json_record = pd.Series(record).to_json()

        # Send the record to the Kinesis Data Stream
        response = kinesis.put_record(
            StreamName=stream_name,
            Data=json_record,
            PartitionKey='partition_key'
        )

        # Introduce a 2-second delay
        time.sleep(2)

    return {
        'statusCode': 200,
        'body': 'Data sent to Kinesis Data Stream'
    }
