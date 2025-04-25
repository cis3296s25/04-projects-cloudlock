from BackEnd.hybrid_crypto import *
import tempfile


def test_setup_directories():
    """Test the setup of directories for storing encrypted files and AES keys."""
    # Create directories
    setup_directories()
    # Check if the directories are created
    assert os.path.exists(AES_DIR)
    assert os.path.exists(ENCRYPTED_FILE_DIR)

def test_hybrid_encrypt():
    """Test that hybrid_encrypt creates expected encrypted output files."""
    #Create a temporary input file with test data
    original_data = b"This is test data for hybrid encryption."
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(original_data)
        input_file_path = temp_file.name

    #hybrid encryption method
    result = hybrid_encrypt(input_file_path)
    assert result is True, "hybrid_encrypt() did not return True"

    #Build expected output file paths for deletion
    base_name = os.path.basename(input_file_path)
    encrypted_file_path = os.path.join(ENCRYPTED_FILE_DIR, base_name + ".enc")
    encrypted_key_path = os.path.join(AES_DIR, base_name + ".key")

    # Clean up
    os.remove(input_file_path)
    if os.path.exists(encrypted_file_path):
        os.remove(encrypted_file_path)
    if os.path.exists(encrypted_key_path):
        os.remove(encrypted_key_path)

def test_hybrid_decrypt():
    """Test that hybrid_decrypt creates expected decrypted output files."""
    # Create a temporary input file with test data
    original_data = b"This is test data for hybrid encryption."
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(original_data)
        input_file_path = temp_file.name

    print("input file path:", input_file_path)

    # Perform hybrid encryption
    hybrid_encrypt(input_file_path)

    base_name = os.path.basename(input_file_path)
    encrypted_file_path = os.path.join(ENCRYPTED_FILE_DIR, base_name + ".enc")
    decrypted_file_path = os.path.join(ENCRYPTED_FILE_DIR, os.path.basename(input_file_path))


    # Perform hybrid decryption
    result = hybrid_decrypt(encrypted_file_path, decrypted_file_path)
    assert result is True, "hybrid_decrypt() did not return True"

    # Check if the decrypted file exists and matches the original data
    with open(decrypted_file_path, "rb") as df:
        decrypted_data = df.read()
        assert decrypted_data == original_data

    # Clean up
    os.remove(input_file_path)
    os.remove(decrypted_file_path)