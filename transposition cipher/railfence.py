from pycipher import Railfence

cipher = Railfence(2)

encrypted = cipher.encipher("meetmeatthetogaparty")
decrypted = cipher.decipher(encrypted)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)