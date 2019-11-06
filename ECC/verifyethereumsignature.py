"""
Verify Ethereum Signature – Example
"""
import eth_keys, binascii

msg = b'Message for signing'
msgSigner = '0xa44f70834a711F0DF388ab016465f2eEb255dEd0' #signer's address?
signature = eth_keys.keys.Signature(binascii.unhexlify('6f0156091cbe912f2d5d1215cc3cd81c0963c8839b93af60e0921b61a19c54300c71006dd93f3508c432daca21db0095f4b16542782b7986f48a5d0ae3c583d401'))

signerPubKey = signature.recover_public_key_from_msg(msg)
print("Singer public key (recovered):", signerPubKey)

signerAddress = signerPubKey.to_checksum_address()
print("Signer address:", signerAddress)
print("Signature value?:", signerAddress == msgSigner)