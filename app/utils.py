import boto3
import os


def get_s3_client():
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    ENDPOINT_URL= os.getenv('ENDPOINT_URL')
    REGION_NAME=os.getenv('REGION_NAME')
    s3 = boto3.client(
        service_name='s3',
        region_name=REGION_NAME,  # Specify the region where your Space is located
        endpoint_url=ENDPOINT_URL,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    return s3
