import pyotp
import qrcode
import os
import json
# basically, creates a google authentication for name_of_user issued by CloudLockTeam that is then made
# into a qr code instead of a link, and basically this random qr code is hooked up to the secret_key
# then the function returns a pointer to the qr code image

#qrview calls authenticate_acct() with username, makes qr code, changes view to tokenview which calls
#verify_user_code() with the correct code from create_one_time_password() to verify user code.

# Defining path and file for randomized qr code each time function is called
BASE_DIR = os.path.dirname(__file__)
QR_DIR = os.path.join(BASE_DIR, "AuthenticationCredentials")
AUTH_PATH = os.path.join(QR_DIR, "authentication_value.json")

def get_secret_key(name_of_user):
    randomized_code = pyotp.random_base32()

    #if os.path.exists(QR_DIR):
        #print("Directory 'AuthenticationCredentials' already established.")
    if not (os.path.exists(QR_DIR)):
        #if the folder doesn't exist, neither does the file. Make one.
        os.makedirs(QR_DIR)

        with open(AUTH_PATH, "w") as qrFile:
            dictionary_written = {name_of_user: randomized_code}
            json.dump(dictionary_written, qrFile, indent=4)
        #print("Directory 'AuthenticationCredentials' and json file created.")

    # ---------------------------------------------------------------------------------------------------------

    with open(AUTH_PATH, 'r') as qrFile:
        data = json.load(qrFile)
        #print("Qr verification link: ", data)

        if data.get(name_of_user, 0) != 0:
            #if it exists
            return data[name_of_user]

    #implied otherwise, it will close the reading stream and open the writing stream to add a new element to the
    #dictionary
    with open(AUTH_PATH, "w") as qrFile:
        data[name_of_user] = randomized_code
        json.dump(data, qrFile, indent=4)
        #print("Qr verification link created")

        return randomized_code

def authenticate_acct(name_of_user, secret_key):
    authentication_link = pyotp.totp.TOTP(secret_key).provisioning_uri(name_of_user,"CloudLockTeam")
    #name_of_user is their google authenticator username and CloudLockTeam is the name of the issuer
    #creates the account for the user that is connected to the secret_key
    #print(authentication_link)

    return authentication_link

def create_one_time_password(secret_key):
    #creates the link for the time-based password based on the secret-key connected to the user
    qrcode_linked = pyotp.TOTP(secret_key)

    return qrcode_linked

def verify_user_code(user_code, correct_otp):
    #verifies the code the user connects with the correct authentication code from the link
    return correct_otp.verify(user_code)

if __name__ == "__main__":
    secret_key = get_secret_key("stellar")
    authenticate_acct("stellar", secret_key)
    qr_key = create_one_time_password(secret_key)
    if verify_user_code(input("Insert a code"), qr_key):
        print("true")
    else:
        print("false")