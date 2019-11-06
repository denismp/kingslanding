"""
EdDSA and Ed25519

This is faster than ECDSA

Edwards-curve Digital Signature Algorithm (EdDSA) uses twisted Edwards curves, designed by D. Bernstein and others
Ed25519 is a cryptosystem, based on ECC (elliptic-curve cryptographic) – http://ed25519.cr.yp.to
    Uses the Edwards's curve Curve25519 (RFC7748)
    x**2 + y**2 = 1 + dx**2y**2

EdDSA (using curve25519) is faster than ECDSA
      (using secp256k1) at similar level of security (even slightly better)

"""
from pure25519 import ed25519_oop

privKey, pubKey = ed25519_oop.create_keypair()
print("Private key (32 bytes):", privKey.to_ascii(encoding='hex'))
print("Public key (32 bytes):", pubKey.to_ascii(encoding='hex'))

msg = b'Message for signing'
signature = privKey.sign(msg, encoding='hex')
print("Signature (64 bytes):", signature)

try:
    pubKey.verify(signature,msg,encoding='hex')
    print("The signature is valid.")
except:
    print("Invalid signature!")