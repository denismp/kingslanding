import hashlib, binascii, hmac

text = 'hello'
data = text.encode("utf8")

sha256hash = hashlib.sha256(data).digest()
print("SHA256:    ", binascii.hexlify(sha256hash))

sha512hash = hashlib.sha512(data).digest()
print("SHA512:    ", binascii.hexlify(sha512hash))

ripemd160 = hashlib.new('ripemd160', data).digest()
print("RIPEMD-160:", binascii.hexlify(ripemd160))

def hmac_sha256(key, msg):
    return hmac.new(key, msg, hashlib.sha256).digest()

key = binascii.unhexlify('fa63f2b4c85af6bed3')
msg = "some message".encode("utf8")
print("HMAC:      ", binascii.hexlify(hmac_sha256(key, msg)))

