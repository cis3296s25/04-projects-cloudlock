import rsa_encryption_utils
import aes_encryption_utils

def hybrid_encrypt(data, rsa_public_key):
    ...

def hybrid_decrypt(encrypted_data, encrypted_aes_key, rsa_private_key):
    ...

def hybrid_encrypt_file(input_file_path, output_file_path, rsa_public_key):
    ...

def hybrid_decrypt_file(input_file_path, output_file_path, rsa_private_key):
    ...
