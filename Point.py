""" This class defines the structure of a point in an elliptic curve context """


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
