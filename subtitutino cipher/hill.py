import hillcipher as hc

key = [[17,17,5],[21,18,21],[2,2,19]]
text = "PAY MORE MONEY"

enc = hc.encrypt(text, key)
dec = hc.decrypt(enc, key)

print(enc)
print(dec)