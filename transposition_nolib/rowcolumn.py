def row_transposition_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    num_cols = len(key)
    num_rows = -(-len(plaintext) // num_cols)  # ceiling division
    plaintext = plaintext.ljust(num_rows * num_cols, 'X')
    grid = [list(plaintext[i*num_cols:(i+1)*num_cols]) for i in range(num_rows)]
    order = sorted(range(num_cols), key=lambda x: key[x])
    ciphertext = ""
    for col in order:
        for row in grid:
            ciphertext += row[col]
    return ciphertext

def row_transposition_decrypt(ciphertext, key):
    num_cols = len(key)
    num_rows = len(ciphertext) // num_cols
    order = sorted(range(num_cols), key=lambda x: key[x])
    grid = [''] * num_cols
    idx = 0
    for col in order:
        grid[col] = ciphertext[idx:idx+num_rows]
        idx += num_rows
    plaintext = ""
    for row in range(num_rows):
        for col in range(num_cols):
            plaintext += grid[col][row]
    return plaintext.rstrip('X')

def column_transposition_encrypt(plaintext, key):
    return row_transposition_encrypt(plaintext, key)

def column_transposition_decrypt(ciphertext, key):
    return row_transposition_decrypt(ciphertext, key)

if __name__ == "__main__":
    key = [3, 1, 4, 2]
    message = "HELLO WORLD"
    enc = row_transposition_encrypt(message, key)
    dec = row_transposition_decrypt(enc, key)
    print(f"Original : {message}")
    print(f"Encrypted: {enc}")
    print(f"Decrypted: {dec}")