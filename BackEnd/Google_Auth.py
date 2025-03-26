import time
from PIL import Image
import pyotp
import qrcode

def authenticate_acct(name_of_user):
    secret_key = "SuitsGreysAnatomyLastOfUsFinalFantasyThisIsNotWhatIExpected"
    authentication_link = pyotp.totp.TOTP(secret_key).provisioning_uri(name_of_user,"CloudLockTeam")
    #name_of_user is their google authenticator username and CloudLockTeam is the name of the issuer

    qrcode.make(authentication_link).save("../Images/current_code.png")
    qrcode_linked = pyotp.TOTP(secret_key)

    #basically, creates a google authentication for name_of_user issued by CloudLockTeam that is then made
    #into a qr code instead of a link, and basically this random qr code is hooked up to the secret_key
    #then the function returns a pointer to the qr code image
    return Image.open(r"../Images/current_code.png")

authenticate_acct("StarfoxAndStellar")