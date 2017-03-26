""" This class defines an elliptic curve """

from random import randint
import math


class Curve:
    """ This method is the constructor of the Curve class
        @:param n The number that must be factorized
        @:return Nothing
    """
    def __init__(self, n, point):
        self.a = randint(0, n - 1)
        self.b = point.get_y()**2 - point.get_x()**3 - (self.a * point.get_x()) % n
        self.delta = ((4 * math.pow(self.a, 3)) + (27 * math.pow(self.b, 2))) % n

    """ This method is the getter for a coefficient variable
        @:param Nothing
        @:return a Return the a coefficient of the curve
    """
    def get_a(self):
        return self.a

    """ This method is the getter for b coefficient variable
        @:param Nothing
        @:return a Return the b coefficient of the curve
    """
    def get_b(self):
        return self.b

    """ This method is the getter for delta discriminant variable
        @:param Nothing
        @:return a Return the delta discriminant of the curve
    """
    def get_delta(self):
        return self.delta

    """ This method represents the curve class as a string to improve readability
        @:param Nothing
        @:return Nothing
    """
    def to_string(self):
        print "Elliptic curve: Y^2 = X^3 + aX + b"
        print "a = " + self.a.__str__()
        print "b = " + self.b.__str__()
        print "delta = " + self.delta.__str__()
