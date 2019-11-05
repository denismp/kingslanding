"""
Elliptic Curves Multiplication in Python
"""
from pycoin.ecdsa.Point import Point
from pycoin.ecdsa.Curve import Curve

"""
This class implements an `Elliptic curve <https://en.wikipedia.org/wiki/Elliptic_curve>`_ intended
for use in `Elliptic curve cryptography <https://en.wikipedia.org/wiki/Elliptic-curve_cryptography>`_

An elliptic curve ``EC<p, a, b>`` for a (usually large) prime p and integers a and b is a
`group <https://en.wikipedia.org/wiki/Group_(mathematics)>`_. The members of the group are
(x, y) points (where x and y are integers over the field of integers modulo p) that satisfy the relation
``y**2 = x**3 + a*x + b (mod p)``. There is a group operation ``+`` and an extra point known
as the "point at infinity" thrown in to act as the identity for the group.

The group operation is a truly marvelous property of this construct, a description of which
this margin is too narrow to contain, so please refer to the links above for more information.

:param p: a prime
:param a: an integer coefficient
:param b: an integer constant
:param order: (optional) the order of the group made up by the points on the
    curve. Any point on the curve times the order is the identity for this
    group (the point at infinity). Although this is optional, it's required
    for some operations.
"""

p=17	# a prime number
a=0		# an integer coefficient
b=7		# an integer constant

curve = Curve(p,a,b)
print("Curve = " , str(curve))

G = Point(15, 13, curve)
print("Point G = ", str(G))

for k in range(0,6):
	print("k = ", str(k), " * Point G = ", str(k * G))