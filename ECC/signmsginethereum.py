"""
Verifying an Ethereum Signature

Ethereum uses secp256k1-based ECDSA signatures
    ECDSA generates deterministically a random point R (see RFC6979)
Ethereum signatures consists of 3 numbers: [v, r, s]
    v – the compressed Y coordinate of the point R (1 byte: 00 or 01)
    r – the X coordinate of the point R (256-bit integer, 32 bytes)
    s – 256-bit integer (32 bytes), calculated from the signer's private key + message hash (Ethereum uses keccak256)
    Typically encoded as 130 hex digits (65 bytes), e.g. 0x…465c5cf4be401
Given an Ethereum signature [v, r, s], the public key can be recovered from [R, s, msgHash]  also the signer's Ethereum address
"""
import eth_keys, binascii

privKey = eth_keys.keys.PrivateKey(binascii.unhexlify('97ddae0f3a25b92268175400149d65d6887b9cefaf28ea2c078e05cdc15a3c0a'))
print("Private key (64 hex digites):", privKey)

signature = privKey.sign_msg(b'Message for signing')

print("Signature: [v = {0}, r = {1}, s = {2}]".format(hex(signature.v), hex(signature.r), hex(signature.s)))
print("Signature (130 hex digits):", signature)