import hmac
import hashlib

message = b"Hello this is a test message"
key = b"secretkey"

mac = hmac.new(key, message, hashlib.sha256)

print("HMAC-SHA256:", mac.hexdigest())