import hashlib, binascii, hmac, os, scrypt, pyaes, pkcs7, secrets
import array as arr

text = 'hello'
data = text.encode("utf8")

print("\nSHA256")
sha256hash = hashlib.sha256(data).digest()
print("SHA256:    ", binascii.hexlify(sha256hash))

print("\nSHA512")
sha512hash = hashlib.sha512(data).digest()
print("SHA512:    ", binascii.hexlify(sha512hash))

print("\nRIPEMD-160")
ripemd160 = hashlib.new('ripemd160', data).digest()
print("RIPEMD-160:", binascii.hexlify(ripemd160))


# HMAC code
def hmac_sha256(key, msg):
    return hmac.new(key, msg, hashlib.sha256).digest()


print("\nHMAC")
key = binascii.unhexlify('fa63f2b4c85af6bed3')
msg = "some message".encode("utf8")
print("HMAC:      ", binascii.hexlify(hmac_sha256(key, msg)))

# Scrypt code
print("\nScrypt")
passwd = "p@$$w0rD~3"
salt = os.urandom(32)
print("Salt:       ", binascii.hexlify(salt))


