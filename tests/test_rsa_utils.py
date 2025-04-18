import unittest
import os
import rsa
from Crypto.Random import get_random_bytes

import rsa_encryption_utils as rsa_module

class TestRSAEncryptionUtils(unittest.TestCase):
    def setUp(self):
        # generating rsa keys
        rsa_module.create_rsa_keys()
    def test_key_files_exist(self):
        self.assertTrue(os.path.exists(rsa_module.PUB_KEY_PATH))
        self.assertTrue(os.path.exists(rsa_module.PRIV_KEY_PATH))

    def test_public_keys_exist(self):
        pub_key = rsa_module.get_rsa_public_key()
        self.assertIsInstance(pub_key, rsa.PublicKey)

    def test_get_rsa_private_key(self):
        priv_key = rsa_module.get_rsa_private_key()
        self.assertIsInstance(priv_key, rsa.PrivateKey)

    def test_encrypt_and_decrypt_aes_key(self):
        original_key = get_random_bytes(16)
        encrypted_key = rsa_module.encrypt_aes_key(original_key)
        self.assertIsNotNone(encrypted_key)

        decrypted_key = rsa_module.decrypt_aes_key(encrypted_key)
        self.assertEqual(original_key, decrypted_key)
    def test_sign_and_verify_signature(self):
        data = "Test message"
        signature = rsa_module.sign_data(data)
        self.assertIsNotNone(signature)

        is_valid = rsa_module.verify_signature(data, signature)
        self.assertTrue(is_valid)

    def test_invalid_signature_fails_verification(self):
        data = "Test message"
        altered_data = "Tampered message"
        signature = rsa_module.sign_data(data)

        self.assertFalse(rsa_module.verify_signature(altered_data, signature))

    def tearDown(self):
        # Optional: Clean up generated keys after test
        try:
            os.remove(rsa_module.PUB_KEY_PATH)
            os.remove(rsa_module.PRIV_KEY_PATH)
            os.rmdir(rsa_module.RSA_DIR)
        except Exception:
            pass


if __name__ == "__main__":
    unittest.main()
