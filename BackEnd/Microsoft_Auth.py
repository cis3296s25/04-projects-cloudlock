import pyotp
import qrcode
import os
import json
# basically, creates a google authentication for name_of_user issued by CloudLockTeam that is then made
# into a qr code instead of a link, and basically this random qr code is hooked up to the secret_key
# then the function returns a pointer to the qr code image

#IF THE FILE EXISTS OPEN FILE, SELECT DICTIONARY YOU WANT FOR USERNAME AND SECRET_KEY
#OTHERWISE< IF USERNAME NOT IN FILE, MAKE NEW QR CODE WITH SCRETKEY
#DONT DELETE THE DAMNED FILE

#secret_key = pyotp.random_base32()
#secret_key = base64.b32encode(b"6THUVVE5BKJG2DOXTSMYDD62BS2EWW2I")
SECRET_KEY = "6THUVVE5BKJG2DOXTSMYDD62BS2EWW2I"
#I think secret_key needs to remain consistent for the userInterface to call these methods separately
#but with the same value to link them together (secret_key)

# Defining path and file for randomized qr code each time function is called
BASE_DIR = os.path.dirname(__file__)
QR_DIR = os.path.join(BASE_DIR, "AuthenticationCredentials")
AUTH_PATH = os.path.join(QR_DIR, "authentication_value.json")

def get_secret_key(name_of_user):
    randomized_code = pyotp.random_base32()

    if os.path.exists(QR_DIR):
        print("Directory 'AuthenticationCredentials' already established.")
    else:
        os.makedirs(QR_DIR)
        print("Directory 'AuthenticationCredentials' created.")

    # ---------------------------------------------------------------------------------------------------------

    if os.path.exists(AUTH_PATH):
        #if the json file exists, open the file with reading permissions and load the information. Based on the
        #username the user inputs, it will traverse the dictionary/Map to find the matching key
        print("QR authentication already established")

        with open(AUTH_PATH, 'r') as qrFile:
            data = json.load(qrFile)
            print("Qr verification link: ", data[name_of_user])

            return data[name_of_user]
    else:
        data = {name_of_user: randomized_code}

        with open(AUTH_PATH, "w") as qrFile:
            json.dump(data, qrFile, indent=4)
            print("Qr verification link created")

            return randomized_code


def get_secret_key(name_of_user):
    randomized_code = pyotp.random_base32()

    if os.path.exists(QR_DIR):
        print("Directory 'AuthenticationCredentials' already established.")
    else:
        #if the folder doesn't exist, neither does the file. Make one.
        os.makedirs(QR_DIR)

        with open(AUTH_PATH, "w") as qrFile:
            dictionary_written = {name_of_user: randomized_code}
            json.dump(dictionary_written, qrFile, indent=4)
        print("Directory 'AuthenticationCredentials' and json file created.")

    # ---------------------------------------------------------------------------------------------------------

    with open(AUTH_PATH, 'r') as qrFile:
        data = json.load(qrFile)
        print("Qr verification link: ", data[name_of_user])

        if data.get(name_of_user, 0) != 0:
            #if it exists
            return data[name_of_user]

    #implied otherwise, it will close the reading stream and open the writing stream to add a new element to the
    #dictionary
    with open(AUTH_PATH, "w") as qrFile:
        data[name_of_user] = randomized_code
        json.dump(data, qrFile, indent=4)
        print("Qr verification link created")

        return randomized_code


def authenticate_acct(name_of_user):
    authentication_link = pyotp.totp.TOTP(SECRET_KEY).provisioning_uri(name_of_user,"CloudLockTeam")
    #name_of_user is their google authenticator username and CloudLockTeam is the name of the issuer
    #creates the account for the user that is connected to the secret_key

    qrcode.make(authentication_link).save("./Images/qr-code.png")

def create_one_time_password():
    #creates the link for the time-based password based on the secret-key connected to the user
    qrcode_linked = pyotp.TOTP(SECRET_KEY)

    return qrcode_linked

def verify_user_code(user_code, correct_otp):
    #verifies the code the user connects with the correct authentication code from the link
    return correct_otp.verify(user_code)