# Small RSA values (easy to remember)
p = 11
q = 13

n = p * q          # 143
phi = (p-1)*(q-1)  # 120

e = 7              # public key
d = 103            # private key

# Encryption : plain * e mod n
def encrypt(plain):
    return pow(plain, e, n)

# Decryption: cipher * d mod n
def decrypt(cipher):
    return pow(cipher, d, n)

# Example
message = 9   # must be < 143

cipher = encrypt(message)
decrypted = decrypt(cipher)

print("Original:", message)
print("Encrypted:", cipher)
print("Decrypted:", decrypted)