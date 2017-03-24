""" This class defines the algorithm of elliptic curve factorization.
    The algorithm is composed by two phase:
        - firstPhase: calculates a non-trivial factor of an integer n, starting from random point
        - secondPhase: calculates a non-trivial factor of an integer n, starting from a finite point
"""
from fractions import gcd

import Smooth
import math
import Point


class Ecm:
    """ This method """

    def __init__(self):
        pass

    @staticmethod
    def first_phase(p, q, n, curve):
        smooth = Smooth.Smooth()
        primes = smooth.get_b1_prime()
        exps = smooth.get_expo()
        lenght = len(primes)

        for i in range(0, lenght):
            power = primes[i] ** exps[i]
            for k in range(0, power):
                if Point.Point.comp_points(p, q):
                    inv = Smooth.inverse(2 * p.get_y(), n)

                    if inv == -1:
                        inv = 2 * p.get_y()
                        inv = inv % n
                        mcd = gcd(inv, n)

                        if 1 < mcd < n:
                            return mcd

                    m = (3 * (p.get_x()**2) + curve.get_a()) * inv
                    m = m % n

                else:
                    inv = Smooth.inverse(q.get_x() - p.get_x(), n)

                    if inv == -1:
                        inv = q.get_x() - p.get_x()
                        inv = inv % n
                        mcd = gcd(inv, n)

                        if 1 < mcd < n:
                            return mcd

                    m = ((q.get_y() - p.get_y()) * inv) % n

                q.set_x((m * m - q.get_x() - p.get_x()) % n)
                if q.get_x() < 0:
                    q.set_x(n + q.get_x())

                q.set_y((-m * (q.get_x() - p.get_x() + p.get_y())) % n)
                if q.get_y() < 0:
                    q.set_y(n + q.get_y())

        return -1
