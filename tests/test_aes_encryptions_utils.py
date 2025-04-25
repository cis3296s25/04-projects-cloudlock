
from BackEnd.aes_encryption_utils import *
import tempfile

def test_generate_aes_key():
    """Test the AES key generation function."""
    key = generate_aes_key()
    assert len(key) == 16  # AES key size should be 16 bytes (128 bits)
    assert isinstance(key, bytes)  # Key should be of type bytes

def test_aes_encrypt():
    """Test the AES encryption function."""
    # Generate a random key
    key = generate_aes_key()
    test_data = b"Test data for AES encryption."

    # Create a temporary file with some data
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Test data for AES encryption.")
        temp_file_path = temp_file.name


    # Encrypt the temporary file
    encrypted_bytes = aes_encrypt(temp_file_path, key)
    assert isinstance(encrypted_bytes, bytes)  # Encrypted data should be bytes
    assert encrypted_bytes != b"Test data for AES encryption." # Encrypted data should not be the same as before
    os.remove(temp_file_path)

def test_aes_decrypt():
    """Test the AES decryption function."""
    # Generate a random key
    key = generate_aes_key()
    test_data = b"Test data for AES encryption."

    # Create a temporary file with some data
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(test_data)
        temp_file_path = temp_file.name

    # Encrypt the temporary file
    encrypted_bytes = aes_encrypt(temp_file_path, key)

    with tempfile.NamedTemporaryFile(delete=False) as temp_file_encrypted:
        temp_file_encrypted.write(encrypted_bytes)
        temp_file_encrypted_path = temp_file_encrypted.name

    # Decrypt the encrypted data
    decrypted_data = aes_decrypt(temp_file_encrypted_path, key)
    assert decrypted_data == test_data  # Decrypted data should match the original data
    os.remove(temp_file_path)
    os.remove(temp_file_encrypted_path)
