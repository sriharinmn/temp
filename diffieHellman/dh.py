# Public values
p = 23   # prime
g = 5    # generator, aka primitive root

# Alice private key
a = 6

# Bob private key
b = 15

# Public keys
A = pow(g, a, p)
B = pow(g, b, p)

print("Alice sends:", A)
print("Bob sends:", B)

# Shared secret
key_alice = pow(B, a, p)
key_bob = pow(A, b, p)

print("Alice's Key:", key_alice)
print("Bob's Key:", key_bob)