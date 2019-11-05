from pycoin.ecdsa.Point import Point
from pycoin.ecdsa.Curve import Curve
from nummaster.basic import sqrtmod

"""
Compressing a Public Key in Python
The reason to compress the Public key is that it is faster.
    The elliptic curves over Fp
        Have at most 2 points per x
        coordinate(odd y and even y)
    A public key P(x,y) can be
    compressed as C(x,odd/even)
        At the curve Y**2 = X**3 + 7 % 17
    P(10,15) == C(10,odd)
        mod_sqrt(x**3 + 7, 17) == y || 17 -y
"""
def compress_key_pair(key_pair):
    return (key_pair[0], key_pair[1] % 2)

def uncompress_key(curve, compressed_key):
    x, is_odd = compressed_key
    p, a, b = curve._p, curve._a, curve._b
    y = sqrtmod(pow(x, 3, p) + a * x + b, p)
    if(bool(is_odd) == bool(y & 1)):
        return (x, y)
    return (x, p - y)

curve = Curve(17,0,7)
p = Point(10,15,curve)
print(f"original key = {p}")

compressed_p = compress_key_pair(p)
print(f"compressed = {compressed_p}")

restored_p = uncompress_key(curve, compressed_p)
print(f"uncompressed = {restored_p}")