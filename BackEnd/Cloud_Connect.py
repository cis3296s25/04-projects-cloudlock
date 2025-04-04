import boto3
import logging
from botocore.exceptions import ClientError
from tkinter import *
import os
import json

# change 'YOUR_ACCESS_KEY_ID' and 'YOUR_SECRET_ACCESS_KEY' for each user
AWS_ACCESS_KEY_ID = 'AWSACCESSKEY'
AWS_SECRET_ACCESS_KEY = 'AWSSECRETKEY'

# Defining path and file for Aws Credential storage
BASE_DIR = os.path.dirname(__file__)
AWS_DIR = os.path.join(BASE_DIR, "AwsCredentials")
AWS_KEY_PATH = os.path.join(AWS_DIR, "credentials.json")

def connectAWS():
    if os.path.exists(AWS_DIR):
        print("Directory 'AwsCredentials' already established.")
    else:
        os.makedirs(AWS_DIR)
        print("Directory 'AwsCrendentials' created.")
    
    if os.path.exists(AWS_KEY_PATH):
        print("Aws credentials already established")
        # testing json file read
        with open(AWS_KEY_PATH, 'r') as awsKeyFile:
            data = json.load(awsKeyFile)
        print("Aws Access Key: ", data["aws_access_key_id"])
    else:
        data = {'aws_access_key_id': AWS_ACCESS_KEY_ID, 'aws_secret_key_id': AWS_SECRET_ACCESS_KEY}
        with open(AWS_KEY_PATH, "w") as awsKeyFile:
            json.dump(data, awsKeyFile, indent=4)
        print("Aws key file created")

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
    # testing Aws Crendential establishment
    connectAWS()
    # testing file upload 
    #upload(r"C:\Users\absei\OneDrive\Documents\cs3296\Final Project\s3FileTest1.txt", "templecloudlockbucket")
    print("Cloud_Connect main")