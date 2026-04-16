def vigenere_encrypt(plaintext, key):
    key = key.upper()
    result = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    result = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

if __name__ == "__main__":
    key = "KEY"
    message = "Hello World"
    enc = vigenere_encrypt(message, key)
    dec = vigenere_decrypt(enc, key)
    print(f"Original : {message}")
    print(f"Encrypted: {enc}")
    print(f"Decrypted: {dec}")