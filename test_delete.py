
import boto3
from botocore.exceptions import ClientError
import logging
import os
S3_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
S3_FOLDER_NAME = 'user_images'
file_name = S3_FOLDER_NAME+'/viterbi.jpg'

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)
try:
    # Check if the object exists in S3
    s3_client.head_object(Bucket=S3_BUCKET_NAME, Key=file_name)
except ClientError as e:
    if e.response['Error']['Code'] == '404':
        # Object does not exist, no need to delete
        print(f"The object '{file_name}' does not exist in S3.")
    else:
        # Handle other errors if needed
        logging.error(e)
else:
    # The object exists, so delete it
    try:
        response = s3_client.delete_object(
            Bucket=S3_BUCKET_NAME, Key=file_name)
        print(response)
    except ClientError as e:
        logging.error(e)
