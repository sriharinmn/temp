from pycipher import Vigenere

cipher = Vigenere("KEY")

encrypted = cipher.encipher("HELLO")
decrypted = cipher.decipher(encrypted)

print(encrypted)
print(decrypted)