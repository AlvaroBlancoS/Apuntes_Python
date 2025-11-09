import os
from Encryption.EncryptionV2 import encrypt, decrypt  # Asegúrate de usar el nombre correcto del módulo donde están definidas las funciones

def main():
    # Definimos una clave y un IV correcto y seguro para la prueba, deben ser 16 bytes para AES-128
    key = os.urandom(16)  # Genera una clave aleatoria de 16 bytes
    iv = os.urandom(16)   # Genera un IV aleatorio de 16 bytes
    
    # Definimos el texto claro (mensaje) que queremos cifrar
    plaintext = b'Este es un texto de prueba'
    
    # Cifrado
    encrypted_data = encrypt(plaintext, key, iv)
    print("Texto Cifrado:", encrypted_data)
    
    # Descifrado
    decrypted_data = decrypt(encrypted_data, key, iv)
    print("Texto Descifrado:", decrypted_data)

if __name__ == '__main__':
    main()
