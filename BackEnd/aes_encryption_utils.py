import os.path
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#Define Absolute Directory of the current file and create a subdirectory for AES keys
BASE_DIR = os.path.dirname(__file__)
AES_DIR = os.path.join(BASE_DIR, "AesKey")

#Define absolute paths for AES key files
AES_KEY_PATH = os.path.join(AES_DIR, "aesKey.pem")


def generate_aes_key():
    """
    This function generates a new AES key and saves it to a file.
    """

    if not os.path.exists(AES_DIR):
        os.makedirs(AES_DIR)
        print("Directory 'AesKey' created.")
    else:
        print("Directory 'AesKey' already exists.")

    # Generate a new AES key if it doesn't exist
    if not os.path.exists(AES_KEY_PATH):
        # Generate a new AES key
        key = get_random_bytes(16)  # AES key size 16 bytes (128 bits)

            # Save Public Key to Pem File
        with open (AES_KEY_PATH, "wb") as key_file:
            key_file.write(key)
            print("AES key generated and saved.")
            print(f"AES Key: {AES_KEY_PATH}")
    else:
        print("AES key file already exists. Skipping key generation.")
        print(f"AES Key: {AES_KEY_PATH}")




def aes_encrypt(data, key):
    ...

def aes_decrypt(encrypted_data, key):
    ...