from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def generate_key_and_iv():
    key = os.urandom(16)
    iv = os.urandom(16)
    return key, iv

def encrypt(plaintext, key, iv):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return ciphertext

def decrypt(ciphertext, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()

    return plaintext.decode()

def main():
    print("AES Encryption and Decryption")
    
    key, iv = generate_key_and_iv()
    print(f"Generated Key: {key.hex()}")
    print(f"Generated IV: {iv.hex()}")

    plaintext = input("\nEnter plaintext to encrypt: ")

    ciphertext = encrypt(plaintext, key, iv)
    print(f"\nCiphertext (hex): {ciphertext.hex()}")

    decrypted_text = decrypt(ciphertext, key, iv)
    print(f"\nDecrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()