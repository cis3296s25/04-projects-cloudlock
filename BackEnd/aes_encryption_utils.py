import os.path
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#Define Absolute Directory of the current file and create a subdirectory for AES keys
BASE_DIR = os.path.dirname(__file__)
AES_DIR = os.path.join(BASE_DIR, "AesKey")
ENCRYPTED_FILE_DIR = os.path.join(BASE_DIR, "EncryptedFiles")

#Define absolute paths for AES key files
AES_KEY_PATH = os.path.join(AES_DIR, "aesKey.key")

# This function generates a new AES key and saves it to a file.
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

        # Save AES key to a file
        with open (AES_KEY_PATH, "wb") as key_file:
            key_file.write(key)
            print("AES key generated and saved.")
            print(f"AES Key: {AES_KEY_PATH}")
    else:
        print("AES key file already exists. Skipping key generation.")
        print(f"AES Key: {AES_KEY_PATH}")

# This function loads the AES key from the file and returns it.
def get_aes_key():
    try:
        with open(AES_KEY_PATH, "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print("AES key file not found.")
        return None

# This function encrypts data using AES encryption with the provided key.
def aes_encrypt(input_path, key):
    """
    Encrypts data using AES encryption with the provided key.
    """

    # Check if the directory for encrypted files exists, if not create it
    if not os.path.exists(ENCRYPTED_FILE_DIR):
        os.makedirs(ENCRYPTED_FILE_DIR)
        print("Directory 'EncryptedFiles' created.")
    else:
        print("Directory 'EncryptedFiles' already exists.")

    # Read the data to be encrypted
    with open (input_path, "rb") as f:
        data = f.read()

    # Encrypt the data using AES GCM mode
    nonce = get_random_bytes(12)  # Generate a random nonce
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    #Determine output file name
    filename = os.path.basename(input_path)
    output_filename = filename + ".enc"
    output_path = os.path.join(ENCRYPTED_FILE_DIR, output_filename)

    with open (output_path, "wb") as f:
        f.write(nonce + tag + ciphertext) # Prepend nonce and tag to the ciphertext
    print(f"Data encrypted and saved to {output_path}")
    return output_path

# This function decrypts data using AES decryption with the provided key.
def aes_decrypt(encrypted_path, key, output_path=None):
    """
    Decrypts a file encrypted with aes_encrypt() using AES-GCM.

    Args:
        encrypted_path (str): Path to the encrypted file.
        key (bytes): AES key used for encryption.
        output_path (str): Optional. If not given, removes ".enc" from input filename.
    """

    with open(encrypted_path, "rb") as f:
        data = f.read()

    nonce = data[:12]           # First 12 bytes = nonce
    tag = data[12:28]           # Next 16 bytes = authentication tag
    ciphertext = data[28:]      # Remaining = encrypted content

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    try:
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    except ValueError:
        print("Decryption failed: Invalid tag or corrupted data.")
        return

    # Determine output filename
    if output_path is None:
        if encrypted_path.endswith(".enc"):
            output_path = encrypted_path[:-4]  # remove .enc
        else:
            output_path = encrypted_path + ".dec"

    with open(output_path, "wb") as f:
        f.write(plaintext)

    print(f"Decrypted data saved to: {output_path}")


if __name__ == "__main__":
    generate_aes_key()
    aes_key = get_aes_key()
    print(f"AES Key: {aes_key}")
    #aes_encrypt(r"C:\Users\guso9\Documents\Public_key_encryption_keys.svg.png", get_aes_key())
    aes_decrypt(r"C:\Users\guso9\Documents\GitHub\04-projects-cloudlock\BackEnd\EncryptedFiles\Public_key_encryption_keys.svg.png.enc", get_aes_key())

