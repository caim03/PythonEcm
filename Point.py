""" This class defines the structure of a point in an elliptic curve context """
import Smooth


class Point:
    """ This method is the constructor of the Point class
        @:param x This is the x coordinate of the point
        @:param y This is the y coordinate of the point
        @:return Nothing
    """

    def __init__(self, x, y, inf):
        self.x = x
        self.y = y
        self.inf = inf

    @staticmethod
    def comp_points(p, q):
        if p.get_x() == q.get_x() and p.get_y() == q.get_y():
            return True
        return False

    @staticmethod
    def sum_points(p, q, curve, n):
        if p.get_inf() == 0:
            return q

        if q.get_inf() == 0:
            return p

        if p.get_x() == q.get_x():
            if (p.get_y() + q.get_y()) % n == 0:
                res_point = Point(0, 1, 0)  # Return Infinity Point
                return res_point

            num = (3 * (p.get_x() ** 2) + curve.get_a()) % n
            den = (2 * p.get_y()) % n

            inv, _, g = Smooth.inverse(den, n)
            if g > 1:
                res_point = Point(0, 0, den)
                return res_point

        else:
            num = (q.get_y() - p.get_y()) % n
            den = (q.get_x() - p.get_x()) % n

            inv, _, g = Smooth.inverse(den, n)
            if g > 1:
                res_point = Point(0, 0, den)
                return res_point

        m = (num * inv) % n

        x3 = (m**2 - q.get_x() - p.get_x()) % n
        y3 = (m * (p.get_x() - x3) - p.get_y()) % n
        res_point = Point(x3, y3, 1)

        return res_point

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

    def get_inf(self):
        return self.inf

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

    def set_inf(self, inf):
        self.inf = inf

    def to_string(self):
        print '(' + self.x.__str__() + ', ' + self.y.__str__() + ', ' + self.inf.__str__() + ')'
