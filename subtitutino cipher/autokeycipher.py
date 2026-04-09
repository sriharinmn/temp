from pycipher import Autokey

cipher = Autokey("KEY")

encrypted = cipher.encipher("HELLO")
decrypted = cipher.decipher(encrypted)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)