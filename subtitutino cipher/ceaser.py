from pycipher import Caesar

cipher = Caesar(key=3)

print(cipher.encipher("HELLO"))
print(cipher.decipher("KHOOR"))