import os
from BackEnd.aes_encryption_utils import generate_aes_key, aes_encrypt, aes_decrypt
from BackEnd.rsa_encryption_utils import (
    create_rsa_keys,
    encrypt_aes_key,
    decrypt_aes_key,
    sign_data,
    verify_signature
)

BASE_DIR = os.path.dirname(__file__)
AES_DIR = os.path.join(BASE_DIR, "EncryptedAesKeys")
ENCRYPTED_FILE_DIR = os.path.join(BASE_DIR, "EncryptedFiles")

def setup_directories():
    """
    This function sets up the necessary directories for storing encrypted files and AES keys.
    """
    # Check if the directory for AES keys exists, if not create it
    if not os.path.exists(AES_DIR):
        os.makedirs(AES_DIR)
        print("Directory 'EncryptedAesKeys' created.")
    else:
        print("Directory 'EncryptedAesKeys' already exists.")

    # Check if the directory for encrypted files exists, if not create it
    if not os.path.exists(ENCRYPTED_FILE_DIR):
        os.makedirs(ENCRYPTED_FILE_DIR)
        print("Directory 'EncryptedFiles' created.")
    else:
        print("Directory 'EncryptedFiles' already exists.")

def hybrid_encrypt(input_file_path):
    """
    This function performs hybrid encryption by first generating a new AES key,
    """

    # Setup directories for storing encrypted files and AES keys
    setup_directories()

    # Check if the directory for RSA keys exists, if not create it with the keys
    create_rsa_keys()

    #generate a new AES key
    aes_key = generate_aes_key()

    # Encrypt the file using AES
    encrypted_data = aes_encrypt(input_file_path, aes_key)

    #encrypt the AES key using RSA
    encrypted_aes_key = encrypt_aes_key(aes_key)


    return {
        "encrypted_file": encrypted_data,
        "encrypted_aes_key": encrypted_aes_key,
    }

def hybrid_decrypt(encrypted_file_path, encrypted_aes_key):

    #Decrypt the AES key using RSA
    aes_key = decrypt_aes_key(encrypted_aes_key)

    # Decrypt the file using AES
    decrypted_data = aes_decrypt(encrypted_file_path, aes_key)

    return decrypted_data




if __name__ == "__main__":
    hybrid_encrypt()