import unittest
import os
from Encryption.EncryptionV2 import encrypt, decrypt  # Importando las funciones directamente

# Clave e IV de prueba; deberían cumplirse después con las normas de seguridad.
key = b'1234567890123456'  # Clave de 16 bytes para AES-128
iv = b'1234567890123456'  # IV de 16 bytes

class TestEncryption(unittest.TestCase):
    def test_key_length(self):
        # Verificar que la longitud de la clave sea correcta para AES.
        self.assertIn(len(key), [16, 24, 32], "La longitud de la clave debe ser de 128, 192 o 256 bits.")

    def test_iv_length(self):
        # Verificar que la longitud del IV sea correcta para AES.
        self.assertEqual(len(iv), 16, "La longitud del IV debe ser de 128 bits.")

    def test_encryption_decryption(self):
        # Verificar el funcionamiento correcto de cifrado y descifrado.
        data = b'This is 16 bytes data'  # Debe ser múltiplo de 16 bytes para CBC con AES
        encrypted = encrypt(data, key, iv)
        decrypted = decrypt(encrypted, key, iv)
        self.assertEqual(data, decrypted, "Los datos descifrados deben ser iguales al original.")

    def test_random_iv(self):
        # Verificar que el IV sea aleatorio e impredecible.
        data = b'This is 16 bytes data'
        iv1 = os.urandom(16)
        iv2 = os.urandom(16)
        encrypted1 = encrypt(data, key, iv1)
        encrypted2 = encrypt(data, key, iv2)
        self.assertNotEqual(iv1, iv2, "Los IV deben ser distintos.")
        self.assertNotEqual(encrypted1, encrypted2, "Los datos cifrados deben diferir con diferentes IVs.")

if __name__ == '__main__':
    unittest.main()
