from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# DES key must be exactly 8 bytes
key = b'8bytekey'

# Create cipher object
cipher = DES.new(key, DES.MODE_ECB)

# Plaintext
plaintext = b'HELLO123'

# Encrypt
ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))
print("Encrypted:", ciphertext.hex())

# Decrypt
cipher_dec = DES.new(key, DES.MODE_ECB)
decrypted = unpad(cipher_dec.decrypt(ciphertext), DES.block_size)
print("Decrypted:", decrypted)