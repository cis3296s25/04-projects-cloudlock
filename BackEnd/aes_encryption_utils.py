import os.path
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#Define Absolute Directory of the current file and create a subdirectory for AES keys
BASE_DIR = os.path.dirname(__file__)
AES_DIR = os.path.join(BASE_DIR, "AesKey")
ENCRYPTED_FILE_DIR = os.path.join(BASE_DIR, "EncryptedFiles")

#Define absolute paths for AES key files
#AES_KEY_PATH = os.path.join(AES_DIR, "aesKey.key")

# This function generates a new AES key and saves it to a file.
# def generate_aes_key():
#     """
#     This function generates a new AES key and saves it to a file.
#     """
#     # Check if the directory for AES keys exists, if not create it
#     if not os.path.exists(AES_DIR):
#         os.makedirs(AES_DIR)
#         print("Directory 'AesKey' created.")
#     else:
#         print("Directory 'AesKey' already exists.")
#
#     # Generate a new AES key if it doesn't exist
#     if not os.path.exists(AES_KEY_PATH):
#         key = get_random_bytes(16)  # AES key size 16 bytes (128 bits)
#
#         # Save AES key to a file
#         with open (AES_KEY_PATH, "wb") as key_file:
#             key_file.write(key)
#             print("AES key generated and saved.")
#             print(f"AES Key: {AES_KEY_PATH}")
#     else:
#         print("AES key file already exists. Skipping key generation.")
#         print(f"AES Key: {AES_KEY_PATH}")

# This function loads the AES key from the file and returns it.

def generate_aes_key(length =16):
    """Generates a new AES key for encryption,length: 16 (AES-128)."""
    return get_random_bytes(length)

# def get_aes_key():
#     try:
#         with open(AES_KEY_PATH, "rb") as key_file:
#             key = key_file.read()
#         return key
#     except FileNotFoundError:
#         print("AES key file not found.")
#         return None

# This function encrypts data using AES encryption with the provided key.
# def aes_encrypt(input_path, key):
#     """
#     Encrypts data using AES encryption with the provided key.
#     """
#
#     # Check if the directory for encrypted files exists, if not create it
#     if not os.path.exists(ENCRYPTED_FILE_DIR):
#         os.makedirs(ENCRYPTED_FILE_DIR)
#         print("Directory 'EncryptedFiles' created.")
#     else:
#         print("Directory 'EncryptedFiles' already exists.")
#
#     # Read the data to be encrypted
#     with open (input_path, "rb") as f:
#         data = f.read()
#
#     # Encrypt the data using AES GCM mode
#     nonce = get_random_bytes(12)  # Generate a random number used once
#     cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)  # Create an AES-GCM cipher object initialized with the key and nonce
#     ciphertext, tag = cipher.encrypt_and_digest(data) # Encrypt the data and generate an authentication tag (returns ciphertext, tag)
#
#     #Determine output file name
#     filename = os.path.basename(input_path)
#     output_filename = filename + ".enc"
#     output_path = os.path.join(ENCRYPTED_FILE_DIR, output_filename)
#
#     # Save the encrypted data to a file
#     with open (output_path, "wb") as f:
#         f.write(nonce + tag + ciphertext) #first 12 bytes = nonce, next 16 bytes = tag, remaining = ciphertext
#     print(f"Data encrypted and saved to {output_path}")
#     return output_path

# This function decrypts data using AES decryption with the provided key.

def aes_encrypt(input_path, key):
    """
    Encrypts data using AES encryption with the provided key.
    """

    # Read the data to be encrypted
    with open (input_path, "rb") as f:
        data = f.read()

    # Encrypt the data using AES GCM mode
    nonce = get_random_bytes(12)  # Generate a random number used once
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)  # Create an AES-GCM cipher object initialized with the key and nonce
    ciphertext, tag = cipher.encrypt_and_digest(data) # Encrypt the data and generate an authentication tag (returns ciphertext, tag)

    return nonce + tag + ciphertext #first 12 bytes = nonce, next 16 bytes = tag, remaining = ciphertext

def aes_decrypt(encrypted_path, key):
    """
    Decrypts a file encrypted with aes_encrypt() using AES-GCM.

    Args:
        encrypted_path (str): Path to the encrypted file.
        key (bytes): AES key used for decryption.

    Returns:
        bytes: The decrypted plaintext data, or None if decryption fails.
    """

    # Check if the encrypted file exists
    if not os.path.exists(encrypted_path):
        print(f"Encrypted file not found: {encrypted_path}")
        return

    # Read the encrypted data
    with open(encrypted_path, "rb") as f:
        data = f.read()

    # Extract nonce, tag, and ciphertext from the encrypted data
    nonce = data[:12]           # First 12 bytes = nonce
    tag = data[12:28]           # Next 16 bytes = authentication tag
    ciphertext = data[28:]      # Remaining = encrypted content
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    # Decrypt the data and verify the tag
    try:
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext
    except ValueError:
        print("Decryption failed: Invalid tag or corrupted data.")
        return

if __name__ == "__main__":
    key = generate_aes_key()
    print("AES Key: ", key)

