import binascii, hmac, os, scrypt, pyaes, pkcs7, secrets

passwd = "p@$$w0rD~3i"

# Symmetric Encryption/Decrption
print("\nSymmetric Encryption")
# Original message
message = 'exercise-cryptography'
message = 'hello world!!!!!'
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
split_key = derived_key.split(maxsplit=1)
# encrpytion_key = split_key[0]
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

encrypter = pyaes.AESModeOfOperationCBC(encrpytion_key, iv=ivArr)
encrypted_message = encrypter.encrypt(message)
print("encrypted_message in hex=", binascii.hexlify(encrypted_message))

decrypter = pyaes.AESModeOfOperationCBC(encrpytion_key , iv=ivArr)
decrypted_message = decrypter.decrypt(encrypted_message)
print("decrypted_message=", decrypted_message)
# Calculate message authentication code (MAC) using HMAC-SHA256(msg, hmac_key)
# message_authentication_code=hmac_sha256(hmac_key,binascii.hexlify(message))

