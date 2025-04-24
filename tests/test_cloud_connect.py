from BackEnd.Cloud_Connect import *
import os
import json

# testing the setAws function - path creation
def test_setAWS_path():
    setAws()
    assert os.path.exists(AWS_DIR) == True

# testing the setAws function - bucket name set
def test_setAws_json_bucket():
    setAws("testBucket", "", "")
    with open(AWS_KEY_PATH, 'r') as awsKeyFile:
            data = json.load(awsKeyFile)
    assert data['bucket_name'] == "testBucket"

# testing the setAws function - access key set
def test_setAws_json_access():
    setAws("", "testAccess", "")
    with open(AWS_KEY_PATH, 'r') as awsKeyFile:
            data = json.load(awsKeyFile)
    assert data['aws_access_key_id'] == "testAccess"

# testing the setAws function - secret key set
def test_setAws_json_secret():
    setAws("", "", "testSecret")
    with open(AWS_KEY_PATH, 'r') as awsKeyFile:
            data = json.load(awsKeyFile)
    assert data['aws_secret_key_id'] == "testSecret"

# testing invalid Aws Credentials upload attempt
def test_uploadS3_failure():
     assert uploadS3(AWS_KEY_PATH, AWS_KEY_PATH) == False
      
# FYI - unable to create secure test of succesful upload to S3 as it would require storage of Aws Secret keys

def tearDown():
    try:
        os.rmdir(AWS_DIR)
    except Exception:
        pass 