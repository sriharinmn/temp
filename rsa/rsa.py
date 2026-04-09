# Hardcoded values (example small RSA)
p = 61
q = 53

n = p * q          # 3233
phi = (p-1)*(q-1)  # 3120

e = 17             # public exponent
d = 2753           # private exponent (precomputed)

# Encryption: c = p^e mod n
def encrypt(plain):
    return pow(plain, e, n)

# Decryption: p = c^d mod n
def decrypt(cipher):
    return pow(cipher, d, n)

# Example
message = 65  # must be < n

cipher = encrypt(message)
decrypted = decrypt(cipher)

print("Original:", message)
print("Encrypted:", cipher)
print("Decrypted:", decrypted)