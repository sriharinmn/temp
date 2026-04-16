def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")
    seen = []
    for ch in key:
        if ch.isalpha() and ch not in seen:
            seen.append(ch)
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            seen.append(ch)
    return [seen[i*5:(i+1)*5] for i in range(5)]

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)

def prepare_text(plaintext):
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    prepared = ""
    i = 0
    while i < len(plaintext):
        prepared += plaintext[i]
        if i + 1 < len(plaintext):
            if plaintext[i] == plaintext[i+1]:
                prepared += 'X'
            else:
                prepared += plaintext[i+1]
                i += 1
        i += 1
    if len(prepared) % 2 != 0:
        prepared += 'X'
    return prepared

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    text = prepare_text(plaintext)
    ciphertext = ""
    for i in range(0, len(text), 2):
        r1, c1 = find_position(matrix, text[i])
        r2, c2 = find_position(matrix, text[i+1])
        if r1 == r2:
            ciphertext += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            ciphertext += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            ciphertext += matrix[r1][c2] + matrix[r2][c1]
    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        r1, c1 = find_position(matrix, ciphertext[i])
        r2, c2 = find_position(matrix, ciphertext[i+1])
        if r1 == r2:
            plaintext += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            plaintext += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            plaintext += matrix[r1][c2] + matrix[r2][c1]
    return plaintext

if __name__ == "__main__":
    key = "MONARCHY"
    message = "HELLO"
    enc = playfair_encrypt(message, key)
    dec = playfair_decrypt(enc, key)
    print(f"Original : {message}")
    print(f"Encrypted: {enc}")
    print(f"Decrypted: {dec}")