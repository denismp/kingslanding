import hashlib, binascii, hmac

text = 'hello'
data = text.encode("utf8")

sha256hash = hashlib.sha256(data).digest()
print("SHA256:    ", binascii.hexlify(sha256hash))

sha512hash = hashlib.sha512(data).digest()
print("SHA512:    ", binascii.hexlify(sha512hash))

ripemd160 = hashlib.new('ripemd160', data).digest()
print("RIPEMD-160:", binascii.hexlify(ripemd160))

hmacSha256 = hmac.new(b'my-secret-key', data, hashlib.sha256)
digest = hmacSha256.hexdigest()
print("HMAC-SHA-256:", digest)
