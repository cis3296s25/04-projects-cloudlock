# CloudLock

CloudLock is a desktop application that uses secure file and image encryption systems. It uses Python and its libraries, such as TkInter, QRCode, PIL, and Boto3 for the AWS cloud connection.

![This is a screenshot.](Images/images.png)

# How to run

- Windows:
  ```bash
  python -m venv .venv
  .venv/Scripts/activate
  pip install -r ./Requirements.txt
  python main.py
  ```
- Linux:
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install -r ./Requirements.txt
  python main.py
  ```

- Complete Google two-factor authentication to log in.
- Select the option to encrypt or decrypt a file.
- Choose the file and enter the public key.
- Press the button to process the file.
- Choose whether to store the encrypted file in the cloud or download it on your local machine.
- Enter cloud credentials and establish AWS connection.
  
# AWS Guide (as of April 2025)

- Create AWS account (free tier compatible)
- Log in to root user account
- Create S3 bucket
- Create IAM user from root user
- Configure access for the newly created IAM user to S3 bucket
- Log in to IAM user
- Validate S3 bucket access
- Create and save IAM user access keys
