import time
import os
from BackEnd.file_search import *
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

end_time = time.time()
start_time = time.time()

# Function to create directories for storing encrypted files and AES keys
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

#Hybrid Encryption Method
def hybrid_encrypt(input_file_path):
    """
    This function encrypts a file using AES encryption and then encrypts the AES key using RSA encryption.

    Args:
        input_file_path (str): The path to the file to be encrypted.
    """
    global start_time, end_time

    start_time = time.time()
    # Setup directories for storing encrypted files and AES keys
    setup_directories()

    # Check if the directory for RSA keys exists, if not create it with the keys
    create_rsa_keys()

    #generate a new AES key
    aes_key = generate_aes_key()

    # Encrypt the file using AES
    encrypted_data = aes_encrypt(input_file_path, aes_key)

    #Save encrypted file
    base_name = os.path.basename(input_file_path)
    encrypted_file_path = os.path.join(ENCRYPTED_FILE_DIR, base_name + ".enc")
    with open (encrypted_file_path, "wb") as ef:
        ef.write(encrypted_data)

    #encrypt the AES key using RSA
    encrypted_aes_key = encrypt_aes_key(aes_key)

    # Save the encrypted AES key to a file
    encrypted_key_path  = os.path.join(AES_DIR, base_name + ".key")
    with open(encrypted_key_path , "wb") as ek:
        ek.write(encrypted_aes_key)

    print(f"Encrypted file saved to: {encrypted_file_path}")
    print(f"Encrypted AES key saved to: {encrypted_key_path}")
    end_time = time.time()

    if os.path.isfile(encrypted_file_path):
        #if the file was successfully made
        return True
    else:
        return False

#Hybrid Decryption Method
def hybrid_decrypt(input_file_path,output_file_path):
    """
    This function decrypts a file using AES decryption and then decrypts the AES key using RSA decryption.

    Args:
        input_file_path (str): The path to the file to be decrypted.
        output_file_path (str): The path to save the decrypted file.

    Returns:
        decrypted_data (bytes): The decrypted data.
    """

    global start_time, end_time

    start_time = time.time()
    #get the base name of the input file, and create paths for the encrypted file and AES key
    base_name = os.path.basename(input_file_path)
    encrypted_file_path = input_file_path

    # Check if the file has the ".enc" extension
    if base_name.endswith(".enc"):
        base_name = base_name[:-4]  # Remove the ".enc" extension to be able to find key file
    encrypted_key_path = os.path.join(AES_DIR, base_name + ".key")

    #Read the encrypted AES key from the file to pass as bytes
    with open (encrypted_key_path, "rb") as ek:
        encrypted_aes_key = ek.read()

    #Decrypt the AES key using RSA
    aes_key = decrypt_aes_key(encrypted_aes_key)

    # Decrypt the file using AES
    decrypted_data = aes_decrypt(encrypted_file_path, aes_key)

    # Save the decrypted data to the specified output file
    with open(output_file_path, "wb") as df:
        df.write(decrypted_data)

    print(f"Decrypted file saved to: {output_file_path}")
    end_time = time.time()

    #Verify the success of decryption
    if os.path.isfile(output_file_path):

        #if successfully decrypted, delete the encrypted file and key
        os.remove(encrypted_file_path)
        os.remove(encrypted_key_path)

        return True
    else:
        return False

def aes_time():
    total_time = (1000*end_time) - (1000*start_time)

    return str(int(total_time)) + "ms" #this is ms!!!

if __name__ == "__main__":
    file_to_encrypt = select_file("*")
    hybrid_encrypt(file_to_encrypt)
    print(aes_time())

    file_to_decrypt = select_file("*.enc")
    hybrid_decrypt(file_to_decrypt, select_save_as(file_to_decrypt))
    print(aes_time())
