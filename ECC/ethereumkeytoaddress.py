"""
Ethereum Addresses and secp256k1

The private key in secp256k1 is 256-bit integer (32 bytes)
Example of Ethereum private key (encoded as 64 hex digits)
    97ddae0f3a25b92268175400149d65d6887b9cefaf28ea2c078e05cdc15a3c0a

The public key is a EC point (2 * 256 bits == 64 bytes)
    7b83ad6afb1209f3c82ebeb08c0c5fa9bf6724548506f2fb4f991e2287a77090177316ca82b0bdf70cd9dee145c3002c0da1d92626449875972a27807b73b42e

Can be compressed to 257 bits (Ethereum uses prefix 02 or 03)
Example of compressed public key (33 bytes / 66 hex digits):
    027b83ad6afb1209f3c82ebeb08c0c5fa9bf6724548506f2fb4f991e2287a77090

The blockchain address in Ethereum is 20 bytes
    Calculated as: last20bytes(keccak256(publicKeyFull))
    Example of Ethereum address (encoded as 40 hex digits):
    a44f70834a711F0DF388ab016465f2eEb255dEd0

    Note: some letters are capital to incorporate a checksum (EIP55)
Digital signatures in secp256k1 are 64 bytes (2 * 32 bytes)
    A pair of two 256-bit numbers: [r, s]
    Calculated by the well-known ECDSA formulas (see RFC6979)
"""
import eth_keys, binascii

privKey = eth_keys.keys.PrivateKey(binascii.unhexlify('97ddae0f3a25b92268175400149d65d6887b9cefaf28ea2c078e05cdc15a3c0a'))
print("Private key (64 hex digits):", privKey)

pubKey = privKey.public_key
print("Public key (plain, 128 hex digits):", pubKey)

pubKeyCompr = '0' + str(2+int(pubKey)%2)+str(pubKey)[2:66]
print("Public key (compressed, 66 hex digits):", pubKeyCompr)

address = pubKey.to_checksum_address()
print("Ethereum address:", address)