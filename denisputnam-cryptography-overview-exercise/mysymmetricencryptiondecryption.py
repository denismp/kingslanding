import hashlib, binascii, hmac, os, scrypt, secrets
import json

from Crypto.Cipher import AES

# HMAC code
def hmac_sha256(key, msg):
    return hmac.new(key, msg, hashlib.sha256).digest()

# # PKCS7 padding
# def pad(m):
#     return m+chr(16-len(m)%16)*(16-len(m)%16)

# PKCS7 padding
def pad(m):
    return m+chr(AES.block_size-len(m)%AES.block_size)*(AES.block_size-len(m)%AES.block_size)


def unpad(ct):
    #return ct[:-ord(ct[-1])]
    return ct[:-ct[-1]]

# PKCS#7 padding
# def pad(message, block_size):
#     padded = message
#     last_block = len(message) % block_size
#     to_pad = block_size - last_block
#     for i in range(to_pad):
#         padded = padded + chr(to_pad)
#     return padded

# def unpad(message, block_size):
#     length = len(message)
#     if length == 0:
#         return message
# 
#     to_pad = ord(message[length - 1])
#     if to_pad > block_size:
#         return message
# 
#     if length < to_pad:
#         return message
# 
#     pad_start = length - to_pad
#     for c in message[pad_start:]:
#         if c != chr(to_pad):
#             return message
# 
#     return message[:pad_start]

passwd = "p@$$w0rD~3i"

# Symmetric Encryption/Decrption
print("\nSymmetric Encryption")
# Original message
message = 'exercise-cryptography'
#message = 'hello world!!!!!'
n = 16384
r = 16
p = 1
buflen = 512

# 256 bit salt
salt = os.urandom(256)
print("salt in hex=", binascii.hexlify(salt))

# Derive a 512-bit key from the password using SCript(n=16384, r=16, p=1 with the random salt(256 bits).
derived_key = scrypt.hash(passwd, salt, N=n, r=r, p=p, buflen=buflen)
print("derived_key=", binascii.hexlify(derived_key))

# Split the derived key into two 256-bit sub-keys
encryption_key = derived_key[:256]
print("encryption_key=", binascii.hexlify(encryption_key))
encrpytion_key = encryption_key[:32] # This can only be 32 bytes max for AES CBC
print("encryption_key=", binascii.hexlify(encrpytion_key))
# hmac_key = split_key[1]
hmac_key = derived_key[256:]
print("hmac_key=", binascii.hexlify(hmac_key))

# Encrypt the message using AES-256(CBC mode with PKCS7 padding) using the encrpytion key.
#   o Use a readom 256-bit IV(initialization vector).
iv = secrets.randbelow(256)
print("iv=", iv)
ivArr = iv.to_bytes(16, byteorder='big')
print("ivArr=", ivArr)
print("ivArr len=", len(ivArr))

# With Crypto libs
cipher = AES.new(encrpytion_key, AES.MODE_CBC, ivArr)
msg = cipher.encrypt(pad(message).encode("utf8"))
print("msg=",binascii.hexlify(msg))
aes = binascii.hexlify(msg)

cipher = AES.new(encrpytion_key, AES.MODE_CBC, ivArr)
msg = cipher.decrypt(msg)
print("msg=", unpad(msg))

print("\nHMAC")
msg = message.encode("utf8")
mac = hmac_sha256(hmac_key, msg)
print("HMAC:      ", binascii.hexlify(mac))

output = {
            'scrypt':{
                    'salt': str(binascii.hexlify(salt)),
                    'n' : str(n),
                    'r' : str(r),
                    'p' : str(p)
                },
            'aes' : str(binascii.hexlify(aes)),
            'iv' : str(binascii.hexlify(ivArr)),
            'mac' : str(binascii.hexlify(mac))
            }


print(json.dumps(output))

#encrypter = pyaes.AESModeOfOperationCBC(encrpytion_key, iv=ivArr)
#encrypted_message = encrypter.encrypt(pad(message))
#print("encrypted_message in hex=", binascii.hexlify(encrypted_message))

#decrypter = pyaes.AESModeOfOperationCBC(encrpytion_key , iv=ivArr)
#decrypted_message = decrypter.decrypt(encrypted_message)
#print("decrypted_message=", upad(decrypted_message))
# Calculate message authentication code (MAC) using HMAC-SHA256(msg, hmac_key)
# message_authentication_code=hmac_sha256(hmac_key,binascii.hexlify(message))

