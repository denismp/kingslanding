import binascii, eth_keys

"""
This exercise can be completed in any other language as well, if the student so chooses, but without the ease of our preconfigured environment.
You can find as a resource attached a preconfigured project, you can use as a starting point in the supported languages.

3.	Ethereum Signature Verifier 
Write a program to verify the Ethereum signature of given  message by given Ethereum address.
 
Input: message + signature + address 
Output: valid / invalid. 

Refer to the provided resources for sample inputs and outputs.

Suggested Python library: eth_keys
Suggested JavaScript library: eth-crypto
"""


def main():
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument('-m', '--msg', default='Hello world!',
                        type=str, help='plain text message')
    parser.add_argument('-s', '--signature',
                        default='6f0156091cbe912f2d5d1215cc3cd81c0963c8839b93af60e0921b61a19c54300c71006dd93f3508c432daca21db0095f4b16542782b7986f48a5d0ae3c583d401',
                        type=str, help='Hex signature')
    parser.add_argument('-a', '--address', default='4Abdd0495671C1aAC55D5bBF4659B1cc237b840e',
                        type=str, help='Ethereum addresss (encoded as 40 hex digits)')
    args = parser.parse_args()

    inputsignature = args.signature
    inputmsg = args.msg
    inputethereumaddress = args.address
    print("inputsignature=", inputsignature)
    print("inputmsg=", inputmsg)
    print("inputethereumaddress=", inputethereumaddress)

    signature = eth_keys.keys.Signature(binascii.unhexlify(inputsignature))
    binaryinputmsg = binascii.hexlify(inputmsg.encode("utf8"))
    # print("binaryinputmsg=", binaryinputmsg)
    signerPubKey = signature.recover_public_key_from_msg(binaryinputmsg)

    signerAddress = signerPubKey.to_checksum_address()
    # print("Signer address:", signerAddress[2:])

    validflag = inputethereumaddress == signerAddress[2:]
    if (validflag == True):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
