import bitcoin, hashlib, binascii

"""
This exercise can be completed in any other language as well, if the student so chooses, but without the ease of our preconfigured environment.
You can find as a resource attached a preconfigured project, you can use as a starting point in the supported languages.

4.	Private Key to Bitcoin Address 
Write a program to generate a Bitcoin address by given Bitcoin private key 
(WIF-encoded). 

Input: BTC Private Key
Output: address 

Refer to the provided resources for sample inputs and outputs.

Suggested Python library: bitcoin
Suggested JavaScript library: bitcoinjs-lib
"""


def private_key_to_public_key(privKeyHex: str) -> (int, int):
    privateKey = int(privKeyHex, 16)
    return bitcoin.fast_multiply(bitcoin.G, privateKey)


def pubkey_to_address(pubKey: str, magic_byte=0) -> str:
    pubKeyBytes = binascii.unhexlify(pubKey)
    sha256val = hashlib.sha256(pubKeyBytes).digest()
    ripemd160val = hashlib.new('ripemd160', sha256val).digest()
    return bitcoin.bin_to_b58check(ripemd160val, magic_byte)


def main():
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument('-k', '--key', default='48f0ba87db8c803933caad92756647f753f07f5a1cd5735a62349b640e81bf94',
                        type=str, help='BTC Private Key')
    args = parser.parse_args()

    inputprivatekey = args.key
    print("inputprivatekey=", inputprivatekey)

    public_key = private_key_to_public_key(inputprivatekey)
    #print("Public key (x,y) coordinates:", public_key)

    compressed_public_key = bitcoin.compress(public_key)
    #print("Public key (hex compressed):", compressed_public_key)

    address = pubkey_to_address(compressed_public_key)
    #print("Compressed Bitcoin address (base58check):", address)

    print("address=", bitcoin.pubkey_to_address(public_key))


if __name__ == "__main__":
    main()
