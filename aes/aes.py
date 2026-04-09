from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# AES key must be 16, 24, or 32 bytes
key = b'1234567890123456'  # 16 bytes (AES-128)

# Initialization Vector (must be 16 bytes)
iv = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_CBC, iv)

plaintext = b'HELLO AES WORLD'

# Encrypt
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
print("Encrypted (hex):", ciphertext.hex())

# Decrypt
cipher_dec = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(cipher_dec.decrypt(ciphertext), AES.block_size)

print("Decrypted:", decrypted.decode())