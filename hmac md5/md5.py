import hmac
import hashlib

# Secret key (must be shared securely)
key = b'secret_key'

# Message
message = b'Hello, this is a test message'

# Generate HMAC-MD5
mac = hmac.new(key, message, hashlib.md5).hexdigest()

print("MAC (HMAC-MD5):", mac)