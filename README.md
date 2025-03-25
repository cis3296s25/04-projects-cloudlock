# Cloud Lock
CloudLock is an application that uses secure file and image encryption systems. It uses Python and its libraries, such as TkInter, QRCode, PIL, and Boto3 for the AWS cloud connection.

![This is a screenshot.](images.png)

# How to run
- (Linux Only)Activate the virtual environment:
  ```bash
  source .venv/bin/activate
  ```
- Download packages:
  ```bash
  pip install -r .venv/Requirements.txt
  ```
- Run the application:
  ```bash
  python UserInterface.py
  ```
- Complete Google two-factor authentication to log in.
- Select the option to encrypt or decrypt a file.
- Choose the file and enter the public key.
- Press the button to process the file.
- Choose whether to store the encrypted file in the cloud or download it on your local machine.
- Enter cloud credentials and establish AWS connection.

# How to contribute
Follow this project board to know the latest status of the project: [http://...]([http://...])  

### How to build
- Use this GitHub repository: ...  
- Specify what branch to use for a more stable release or for cutting edge development.  
- Use IntelliJ 11  
- Specify additional libraries to download if needed  
- Indicate which file and target to compile and run  
- Describe what is expected to happen when the app starts  

# Test pull request
