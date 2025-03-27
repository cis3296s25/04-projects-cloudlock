import boto3
import logging
from botocore.exceptions import ClientError
from tkinter import *

# change 'YOUR_ACCESS_KEY_ID' and 'YOUR_SECRET_ACCESS_KEY' for each user
AWS_ACCESS_KEY_ID = 'YOUR_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'YOUR_SECRET_ACCESS_KEY'

def upload(file_path, bucket_name, file_key=None):
    bucket_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    # file_key = what will show in s3
    if file_key is None:
        file_key = file_path

    try:
        bucket_client.upload_file(
            Filename=file_path,
            Bucket=bucket_name,
            Key=file_key
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == '__main__':
    # testing file upload 
    upload(r"C:\Users\absei\OneDrive\Documents\cs3296\Final Project\s3FileTest1.txt", "templecloudlockbucket")
    print("Cloud_Connect main")