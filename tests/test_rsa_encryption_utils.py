from BackEnd.aes_encryption_utils import generate_aes_key
from BackEnd.rsa_encryption_utils import *


def test_create_rsa_keys():
    """
    Test the creation of RSA Keys
    """
    # Create RSA Keys
    create_rsa_keys()
    # Check if the keys are created
    assert os.path.exists(PRIV_KEY_PATH)
    assert os.path.exists(PUB_KEY_PATH)

def test_get_rsa_public_key():
    """
    Test Get RSA Public Key
    """

    # Create RSA Keys
    create_rsa_keys()
    public_key = get_rsa_public_key()
    with open (PUB_KEY_PATH, "rb") as publicKeyFile:
        public_key_from_file = rsa.PublicKey.load_pkcs1(publicKeyFile.read())
    # Check if the public key is loaded
    assert public_key is not None
    assert public_key_from_file == public_key

def test_get_rsa_private_key():
    """
    Test Get RSA Private Key
    """
    #Create RSA Keys
    create_rsa_keys()
    private_key = get_rsa_private_key()
    with open (PRIV_KEY_PATH,"rb") as privateKeyFile:
        private_key_from_file = rsa.PrivateKey.load_pkcs1(privateKeyFile.read())

    # Check if the private key is loaded
    assert private_key is not None
    assert private_key_from_file == private_key

def test_encrypt_aes_key():
    """
    Test Encrypt AES Key
    """
    # Create RSA Keys
    create_rsa_keys()
    aes_key = generate_aes_key()
    encrypted_aes_key = encrypt_aes_key(aes_key)
    # Check if the AES key is encrypted and decrypted correctly
    assert encrypted_aes_key != aes_key

def test_decrypt_aes_key():
    """
    Test Decrypt AES Key
    """
    # Create RSA Keys
    create_rsa_keys()
    aes_key = generate_aes_key()
    encrypted_aes_key = encrypt_aes_key(aes_key)
    private_key = get_rsa_private_key()
    decrypted_aes_key = decrypt_aes_key(encrypted_aes_key)
    # Check if the AES key is decrypted correctly
    assert decrypted_aes_key is not None
    assert decrypted_aes_key == aes_key

