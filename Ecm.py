""" This class defines the algorithm of elliptic curve factorization.
    The algorithm is composed by two phase:
        - firstPhase: calculates a non-trivial factor of an integer n, starting from random point
        - secondPhase: calculates a non-trivial factor of an integer n, starting from a finite point
"""
from fractions import gcd
import Smooth
from Point import Point


class Ecm:
    """ This method """

    def __init__(self):
        pass

    @staticmethod
    def first_phase(p, q, n, curve, smooth):
        primes = smooth.get_b1_prime()
        exps = smooth.get_expo()
        length = len(primes)

        for i in range(0, length):
            power = primes[i] ** exps[i]
            for k in range(0, power):
                res = Point.sum_points(p, q, curve, n)
                if res > 0:
                    return res
                if res == -1:
                    return -1
        return -1

    @staticmethod
    def second_phase(q, n, curve, smooth):
        primes = smooth.get_b2_prime()
        length = len(primes)
        temp = Point(q.get_x(), q.get_y())

        for i in range(0, length):
            for k in range(0, primes[i]):
                res = Point.sum_points(q, temp, curve, n)
                if res > 0:
                    return res
                if res == -1:
                    return -1
        return -1