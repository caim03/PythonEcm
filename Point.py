""" This class defines the structure of a point in an elliptic curve context """
from fractions import gcd

import Smooth


class Point:
    """ This method is the constructor of the Point class
        @:param x This is the x coordinate of the point
        @:param y This is the y coordinate of the point
        @:return Nothing
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def comp_points(p, q):
        if p.get_x() == q.get_x() and p.get_y() == q.get_y():
            return True
        return False

    @staticmethod
    def sum_points(p, q, curve, n):
        if Point.comp_points(p, q):
            inv = Smooth.inverse(2 * p.get_y(), n)
            if inv == -1:
                inv = 2 * p.get_y()
                inv = inv % n
                mcd = gcd(inv, n)

                if 1 < mcd < n:
                    return mcd

                if mcd == 1 or mcd == n:
                    return -1

            m = (3 * (p.get_x() ** 2) + curve.get_a()) * inv
            m = m % n

        else:
            inv = Smooth.inverse(q.get_x() - p.get_x(), n)
            if inv == -1:
                inv = q.get_x() - p.get_x()
                inv = inv % n
                if inv < 0:
                    inv = n + inv
                mcd = gcd(inv, n)
                if 1 < mcd < n:
                    return mcd

                if mcd == 1 or mcd == n:
                    return -1

            m = ((q.get_y() - p.get_y()) * inv) % n

        q.set_x((m**2 - q.get_x() - p.get_x()) % n)
        if q.get_x() < 0:
            q.set_x(n + q.get_x())
        q.set_y((-m * (q.get_x() - p.get_x()) - p.get_y()) % n)
        if q.get_y() < 0:
            q.set_y(n + q.get_y())

    """ This method is the getter for x coordinate variable
        @:param Nothing
        @:return x Return the x coordinate of the point
    """

    def get_x(self):
        return self.x

    """ This method is the getter for y coordinate variable
        @:param Nothing
        @:return y Return the y coordinate of the point
    """

    def get_y(self):
        return self.y

    """ This method is the setter for x coordinate variable
        @:param x This is the x coordinate of the point
        @:return Nothing
    """

    def set_x(self, x):
        self.x = x

    """ This method is the setter for y coordinate variable
        @:param y This is the y coordinate of the point
        @:return Nothing
    """

    def set_y(self, y):
        self.y = y

    """ This method represents the point class as a string to improve readability
        @:param Nothing
        @:return Nothing
    """

    def to_string(self):
        print '(' + self.x.__str__() + ', ' + self.y.__str__() + ')'
