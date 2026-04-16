def railfence_encrypt(plaintext, rails):
    fence = [[] for _ in range(rails)]
    rail, direction = 0, 1
    for char in plaintext:
        fence[rail].append(char)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    return ''.join(''.join(r) for r in fence)

def railfence_decrypt(ciphertext, rails):
    n = len(ciphertext)
    pattern = []
    rail, direction = 0, 1
    for i in range(n):
        pattern.append(rail)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    indices = sorted(range(n), key=lambda i: pattern[i])
    result = [''] * n
    for i, char in zip(indices, ciphertext):
        result[i] = char
    return ''.join(result)

if __name__ == "__main__":
    message = "HELLO WORLD"
    rails = 3
    enc = railfence_encrypt(message, rails)
    dec = railfence_decrypt(enc, rails)
    print(f"Original : {message}")
    print(f"Encrypted: {enc}")
    print(f"Decrypted: {dec}")