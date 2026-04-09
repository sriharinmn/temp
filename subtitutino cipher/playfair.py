from pycipher import Playfair

cipher = Playfair("MONARCHYBDEFGIKLPQSTUVWXZ")

encrypted = cipher.encipher("hello")
decrypted = cipher.decipher(encrypted)

print(encrypted)
print(decrypted)