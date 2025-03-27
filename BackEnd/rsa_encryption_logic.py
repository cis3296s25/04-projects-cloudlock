import rsa
import os
# This module handles RSA encryption and decryption logic using the rsa library.

# Get the directory of the current file and create a subdirectory for RSA keys
BASE_DIR = os.path.dirname(__file__)
RSA_DIR = os.path.join(BASE_DIR, "RsaKeys")

# Define paths for public and private key files
PUB_KEY_PATH = os.path.join(RSA_DIR, "publicKey.pem")
PRIV_KEY_PATH = os.path.join(RSA_DIR, "privateKey.pem")

def create_rsa_keys():
    """
    This function generates a new RSA key pair and saves them to PEM files.
    """

    # Check if the directory for RSA keys exists, if not create it
    if not os.path.exists(RSA_DIR):
        os.makedirs(RSA_DIR)
        print("Directory 'RsaKeys' created.")
    else:
        print("Directory 'RsaKeys' already exists.")

    # Generate a new RSA key pair if they don't exist (public and private keys)
    if not os.path.exists(PUB_KEY_PATH) or not os.path.exists(PRIV_KEY_PATH):
        publicKey, privateKey = rsa.newkeys(1024) #1024 bits is a common key size for RSA

        # Save Public Key to Pem File
        with open(PUB_KEY_PATH, "wb") as publicKeyFile:
            publicKeyFile.write(publicKey.save_pkcs1(format='PEM'))

        # Save Private Key to Pem File
        with open(PRIV_KEY_PATH, "wb") as privateKeyFile:
            privateKeyFile.write(privateKey.save_pkcs1(format='PEM'))

        print("RSA keys generated and saved.")
        print(f"Public Key: {PUB_KEY_PATH}")
        print(f"Private Key: {PRIV_KEY_PATH}")
    else:
        print("RSA key files already exist. Skipping key generation.")
        print(f"Public Key: {PUB_KEY_PATH}")
        print(f"Private Key: {PRIV_KEY_PATH}")

# This function loads the RSA public key from the PEM file and returns it.
def get_rsa_public_key():
    try:
        with open(PUB_KEY_PATH, "rb") as publicKeyFile:
            public_key = rsa.PublicKey.load_pkcs1(publicKeyFile.read())
        return public_key
    except FileNotFoundError:
        print("Public key file not found. Please generate the keys first.")
        return None

# This function loads the RSA private key from the PEM file and returns it.
def get_rsa_private_key():
    try:
        with open(PRIV_KEY_PATH, "rb") as privateKeyFile:
            private_key = rsa.PrivateKey.load_pkcs1(privateKeyFile.read())
        return private_key
    except FileNotFoundError:
        print("Private key file not found. Please generate the keys first.")
        return None


#TODO: Implement encryption and decryption functions using the loaded keys.

#TODO: Implement Signature verification and signing functions using the loaded keys.

#TODO: Implement Verify functions to check the integrity of the data using the public key.

if __name__ == "__main__":
    create_rsa_keys()
    print(get_rsa_public_key())
    print(get_rsa_private_key())