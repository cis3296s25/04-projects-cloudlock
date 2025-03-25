import boto3
import logging
from botocore.exceptions import ClientError
from tkinter import *

def upload(file_path, bucket_name, file_key=None):
    bucket_client = boto3.client("s3")

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
    #upload("C:\Users\absei\OneDrive\Documents\cs3296\Final Project\s3FileTest1.txt", "templecloudlockbucket")
    print("Cloud_Connect main")