import rsa
import os
from Crypto.Random import get_random_bytes

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
def encrypt_aes_key(aes_key):
    """
    Encrypts the given data using the RSA public key.
    """
    public_key = get_rsa_public_key()
    if public_key:
        encrypted_data = rsa.encrypt(aes_key, public_key)
        return encrypted_data
    else:
        print("Public key not found for encryption.")
        return None

#Decrypts the given data using the RSA private key.
def decrypt_aes_key(encrypted_aes_key):
    """
    Decrypts the given data using the RSA private key.
    """
    private_key = get_rsa_private_key()
    if private_key:
        decrypted_aes_key = rsa.decrypt(encrypted_aes_key, private_key)
        return decrypted_aes_key
    else:
        print("Private key not found for decryption.")
        return None

# Signs the given data using the RSA private key.
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

# Verifies the given signature using the RSA public key.
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

#this is the main function to test the RSA encryption and decryption logic.
if __name__ == "__main__":

    # Create RSA keys if they don't exist
    create_rsa_keys()

    # Print RSA keys for reference
    print("Public Key:", get_rsa_public_key())
    print("Private Key:", get_rsa_private_key())

    # 1. Generate a new AES key (random 16-byte key)
    aes_key = get_random_bytes(16)
    print(f"Original AES Key: {aes_key}")

    # 2. Encrypt the AES key using RSA
    encrypted_key = encrypt_aes_key(aes_key)
    print(f"Encrypted AES Key: {encrypted_key}")

    # 3. Decrypt the AES key using RSA
    decrypted_key = decrypt_aes_key(encrypted_key)
    print(f"Decrypted AES Key: {decrypted_key}")

    # 4. Check if the original and decrypted keys match
    if aes_key == decrypted_key:
        print("AES key decrypted successfully and matches the original.")
    else:
        print("Decrypted AES key does NOT match the original.")

    #Sign and verify a string message
    message = "Hello, this is a test message."
    signature = sign_data(message)
    print(f"Signature: {signature}")

    is_verified = verify_signature(message, signature)
    print(f"Signature verified: {is_verified}")

    is_not_verified = verify_signature("Hello this is a test message.", signature)
    print(f"Modified message verification failed: {not is_not_verified}")