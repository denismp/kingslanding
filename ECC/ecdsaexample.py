"""
ECC Parameters and secp256k1

ECC operates with a set of EC domain parameters:
T = (p, a, b, G, n, h)
Prime field (prime p), elliptic equation (a, b), base point G(xG, yG), order of G (prime n), cofactor (h)
The secp256k1 standard (used in Bitcoin) defines 256-bit elliptic-curves cryptosystem:
Prime field (p) = 2256 - 232 - 977; Equation: y2 = x3 + 7 (a = 0, b = 7)
G = 0x79BE667E …; n =  0xFFF…D0364141; h = 1

Learn more at: http://www.secg.org/sec2-v2.pdf, https://en.bitcoin.it/wiki/Secp256k1

What is a Digital Signature?

Digital signature
Cryptographic proof for message authenticity
Authentication
Signed by certain private key
Verified by the corresponding public key
Non-repudiation
The sender cannot deny the signing later
Integrity
The message cannot be altered after signing

ECDSA: Sign Messages and Verify Signatures

The Elliptic-Curves Digital Signature Algorithm (ECDSA) provides signing by private key + verifying signature by public key
Signing a message
sign(private_key, msg)  signature (the signature is a pair of numbers [r, s])
Performs some math, based on elliptic curve calculations
Verifying a message signature
verify(public_key, msg, signature)  true / false
Performs some math, based on elliptic curve calculations

"""
from pycoin.ecdsa.secp256k1 import secp256k1_generator
import hashlib

def keccak_hash(msg):
    hash_bytes = hashlib.sha3_256(msg.encode("utf8")).digest()
    return int.from_bytes(hash_bytes, byteorder = "big")

msg = "some message"
msg_hash = keccak_hash(msg)

private_key = 9999999999999999999999999999999999999999999999
signature = secp256k1_generator.sign(private_key, msg_hash)
print("signature = ", str(signature))

public_key = secp256k1_generator * private_key
print("public key = ", str(public_key))

valid = secp256k1_generator.verify(public_key,msg_hash, signature)
print("Signature valid? ", str(valid))

tampered_msg_hash = keccak_hash("tampered msg")
valid = secp256k1_generator.verify(public_key, tampered_msg_hash, signature)
print("Signature (tampered msg) valid? ", str(valid))