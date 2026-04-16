def caesar_encrypt(plaintext, shift):
    result = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

if __name__ == "__main__":
    message = "Hello World"
    shift = 3
    enc = caesar_encrypt(message, shift)
    dec = caesar_decrypt(enc, shift)
    print(f"Original : {message}")
    print(f"Encrypted: {enc}")
    print(f"Decrypted: {dec}")