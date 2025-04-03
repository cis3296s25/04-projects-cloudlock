import time
from PIL import Image
import pyotp
import qrcode
import random

secret_key = "SuitsGreysAnatomyLastOfUsFinalFantasyThisIsNotWhatIExpected"
#I think secret_key needs to remain consistent for the userInterface to call these methods separately
#but with the same value to link them together (secret_key)

def create_one_time_password():
    qrcode_linked = pyotp.TOTP(secret_key)

    # basically, creates a google authentication for name_of_user issued by CloudLockTeam that is then made
    # into a qr code instead of a link, and basically this random qr code is hooked up to the secret_key
    # then the function returns a pointer to the qr code image

    return qrcode_linked

def authenticate_acct(name_of_user):
    authentication_link = pyotp.totp.TOTP(secret_key).provisioning_uri(name_of_user,"CloudLockTeam")
    #name_of_user is their google authenticator username and CloudLockTeam is the name of the issuer

    qrcode.make(authentication_link).save("../Images/qr-code.png")