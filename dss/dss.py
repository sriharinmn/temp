from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

from cryptography.exceptions import InvalidSignature

# =========================
# 1. Key Generation
# =========================
private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

# =========================
# 2. Message
# =========================
message = b"Hello, this is a secure message"

# =========================
# 3. Signing
# =========================
signature = private_key.sign(
    message,
    hashes.SHA256()
)

print("Signature:", signature.hex())

# =========================
# 4. Verification
# =========================
try:
    public_key.verify(
        signature,
        message,
        hashes.SHA256()
    )
    print("Signature is VALID")
except InvalidSignature:
    print("Signature is INVALID")