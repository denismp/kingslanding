import binascii, eth_keys

"""
This exercise can be completed in any other language as well, if the student so chooses, but without the ease of our preconfigured environment.
You can find as a resource attached a preconfigured project, you can use as a starting point in the supported languages.
 
1.	Ethereum Signature Creator 
Write a program to calculate an Ethereum signature	 by given message and private key.
 
Input: 256-bit private key + input text message. 
Output: signature + message. 

Refer to the provided resources for sample inputs and outputs.

Suggested Python library: eth_keys
Suggested JavaScript library: eth-crypto

Ethereum uses secp256k1-based ECDSA signatures
    ECDSA generates deterministically a random point R (see RFC6979)
Ethereum signatures consists of 3 numbers: [v, r, s]
    v – the compressed Y coordinate of the point R (1 byte: 00 or 01)
    r – the X coordinate of the point R (256-bit integer, 32 bytes)
    s – 256-bit integer (32 bytes), calculated from the signer's private key + message hash (Ethereum uses keccak256)
    Typically encoded as 130 hex digits (65 bytes), e.g. 0x…465c5cf4be401
Given an Ethereum signature [v, r, s], the public key can be recovered from [R, s, msgHash]  also the signer's Ethereum address
"""

def main():
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument('-k', '--key', default='97ddae0f3a25b92268175400149d65d6887b9cefaf28ea2c078e05cdc15a3c0a',
                        type=str, help='256 bit private key')
    parser.add_argument('-m', '--msg', default='Hello world!',
                        type=str, help='plain text message')
    args = parser.parse_args()

    inputkey = args.key # this is a private key
    inputmsg = args.msg # this is a plain text message
    print("inputkey=", inputkey)
    print("inputmsg=", inputmsg)

    privKey = eth_keys.keys.PrivateKey(
        binascii.unhexlify(inputkey))
    #print("Private key (64 hex digites):", privKey)

    binaryinputmsg = binascii.hexlify(inputmsg.encode("utf8"))
    signature = privKey.sign_msg(binaryinputmsg)

    #print("Signature: [v = {0}, r = {1}, s = {2}]".format(hex(signature.v), hex(signature.r), hex(signature.s)))
    print("Signature (130 hex digits):", signature)
    print("Message in hex:", binaryinputmsg)
    print("Message:", binascii.unhexlify(binaryinputmsg))

if __name__ == "__main__":
    main()
