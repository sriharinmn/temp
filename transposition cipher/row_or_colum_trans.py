from pycipher import ColTrans

cipher = ColTrans("EDBCFGH") # 4312567

encrypted = cipher.encipher("ATTACKPOSTPONEDUNTILTWOAMXYZ")
decrypted = cipher.decipher(encrypted)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)