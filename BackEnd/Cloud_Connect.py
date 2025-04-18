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

def setAws(bucket_name, access_key, secret_key):
    if not os.path.exists(AWS_DIR):
        os.makedirs(AWS_DIR)
        print("Directory 'AwsCrendentials' created.")
    
    if os.path.exists(AWS_KEY_PATH):
        if len(bucket_name) != 0:
            with open(AWS_KEY_PATH, 'r') as awsKeyFile:
                data = json.load(awsKeyFile)
            data['bucket_name'] = bucket_name
            with open(AWS_KEY_PATH, 'w') as awsKeyFile:
                json.dump(data, awsKeyFile, indent=4)
        if len(access_key) != 0:
            with open(AWS_KEY_PATH, 'r') as awsKeyFile:
                data = json.load(awsKeyFile)
            data['aws_access_key_id'] = access_key
            with open(AWS_KEY_PATH, 'w') as awsKeyFile:
                json.dump(data, awsKeyFile, indent=4)
        if len(secret_key) != 0:
            with open(AWS_KEY_PATH, 'r') as awsKeyFile:
                data = json.load(awsKeyFile)
            data['aws_secret_key_id'] = secret_key
            with open(AWS_KEY_PATH, 'w') as awsKeyFile:
                json.dump(data, awsKeyFile, indent=4)
    else:
        data = {'bucket_name': bucket_name, 'aws_access_key_id': access_key, 'aws_secret_key_id': secret_key}
        with open(AWS_KEY_PATH, "w") as awsKeyFile:
            json.dump(data, awsKeyFile, indent=4)

def uploadS3(file_path, file_key):
    try:
        if os.path.exists(AWS_KEY_PATH):
            with open(AWS_KEY_PATH, 'r') as awsKeyFile:
                data = json.load(awsKeyFile)
            bucket_client = boto3.client('s3', aws_access_key_id=data['aws_access_key_id'], aws_secret_access_key=data['aws_secret_key_id'])
            bucket_client.upload_file(
                Filename=file_path,
                Bucket=data['bucket_name'],
                Key=file_key
            )
        else: 
            print("Aws credentials not established")
            return False
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == '__main__':
    # testing Aws Crendential establishment
    setAws()
    # testing file upload 
    #uploadS3(r"C:\Users\absei\OneDrive\Documents\cs3296\Final Project\s3FileTest1.txt")
    print("Cloud_Connect main")