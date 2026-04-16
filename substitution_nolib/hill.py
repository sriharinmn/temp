def mod_inverse(a, m=26):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mult_mod(matrix, vector, mod=26):
    size = len(vector)
    result = []
    for row in matrix:
        val = sum(row[j] * vector[j] for j in range(size)) % mod
        result.append(val)
    return result

def matrix_inverse_2x2(matrix, mod=26):
    a, b = matrix[0]
    c, d = matrix[1]
    det = (a * d - b * c) % mod
    det_inv = mod_inverse(det, mod)
    if det_inv is None:
        raise ValueError("Matrix is not invertible under mod 26")
    inv = [
        [(d * det_inv) % mod, (-b * det_inv) % mod],
        [(-c * det_inv) % mod, (a * det_inv) % mod]
    ]
    return inv

def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace(" ", "")
    size = len(key_matrix)
    if len(plaintext) % size != 0:
        plaintext += 'X' * (size - len(plaintext) % size)
    ciphertext = ""
    for i in range(0, len(plaintext), size):
        block = [ord(c) - ord('A') for c in plaintext[i:i+size]]
        enc_block = matrix_mult_mod(key_matrix, block)
        ciphertext += ''.join(chr(n + ord('A')) for n in enc_block)
    return ciphertext

def hill_decrypt(ciphertext, key_matrix):
    inv_matrix = matrix_inverse_2x2(key_matrix)
    plaintext = ""
    size = len(key_matrix)
    for i in range(0, len(ciphertext), size):
        block = [ord(c) - ord('A') for c in ciphertext[i:i+size]]
        dec_block = matrix_mult_mod(inv_matrix, block)
        plaintext += ''.join(chr(n + ord('A')) for n in dec_block)
    return plaintext

if __name__ == "__main__":
    key_matrix = [[3, 3], [2, 5]]
    message = "HELP"
    enc = hill_encrypt(message, key_matrix)
    dec = hill_decrypt(enc, key_matrix)
    print(f"Original : {message}")
    print(f"Encrypted: {enc}")
    print(f"Decrypted: {dec}")