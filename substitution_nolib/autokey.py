def autokey_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper()
    full_key = key + plaintext
    ciphertext = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(full_key[i]) - ord('A')
            encrypted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += encrypted
    return ciphertext

def autokey_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""
    full_key = list(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(full_key[i]) - ord('A')
            decrypted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plaintext += decrypted
            full_key.append(decrypted)
    return plaintext

if __name__ == "__main__":
    key = "KEY"
    message = "HELLO"
    enc = autokey_encrypt(message, key)
    dec = autokey_decrypt(enc, key)
    print(f"Original : {message}")
    print(f"Encrypted: {enc}")
    print(f"Decrypted: {dec}")