import rsa
import os

# This module handles RSA encryption and decryption logic using the rsa library.

# Get the absolute directory of the current file and create a subdirectory for RSA keys
BASE_DIR = os.path.dirname(__file__)
RSA_DIR = os.path.join(BASE_DIR, "RsaKeys")

# Define absolute paths for public and private key files
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

# Encrypts the given data using the RSA public key.
def encrypt_data(data):
    """
    Encrypts the given data using the RSA public key.
    """
    public_key = get_rsa_public_key()
    if public_key:
        encrypted_data = rsa.encrypt(data.encode('utf-8'), public_key)
        return encrypted_data
    else:
        print("Public key not found for encryption.")
        return None

#Decrypts the given data using the RSA private key.
def decrypt_data(encrypted_data):
    """
    Decrypts the given data using the RSA private key.
    """
    private_key = get_rsa_private_key()
    if private_key:
        decrypted_data = rsa.decrypt(encrypted_data, private_key).decode('utf-8')
        return decrypted_data
    else:
        print("Private key not found for decryption.")
        return None

#TODO: Implement Signature verification and signing functions using the loaded keys.
def sign_data(data):
    """
    Signs the given data using the RSA private key.
    """
    private_key = get_rsa_private_key()
    if private_key:
        signature = rsa.sign(data.encode('utf-8'), private_key, 'SHA-256')
        return signature
    else:
        print("Private key not found for signing.")
        return None

#TODO: Implement Verify functions to check the integrity of the data using the public key.
def verify_signature(data, signature):
    """
    Verifies the given signature using the RSA public key.
    """
    public_key = get_rsa_public_key()
    if public_key:
        try:
            rsa.verify(data.encode('utf-8'), signature, public_key)
            return True
        except rsa.VerificationError:
            return False
    else:
        print("Public key not found for verification.")
        return False

if __name__ == "__main__":
    create_rsa_keys()
    print(get_rsa_public_key())
    print(get_rsa_private_key())
    message = "Hello, this is a test message."
    signature = sign_data(message)
    print(f"this is the signature:{signature}")
    encrypted_message = encrypt_data(message)
    print(f"this is the encrypted message:{encrypted_message}")
    decrypted_message = decrypt_data(encrypted_message)
    print(f"this is the decrypted message:{decrypted_message}")
    is_verified = verify_signature(message, signature)
    print(f"this is the verified message:{is_verified}")
    is_not_verified = verify_signature("Hello this is a test message.", signature)
    print (f"this is the not verified message:{is_not_verified}")


