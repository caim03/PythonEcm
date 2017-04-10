""" 
    This class defines the algorithm of elliptic curve factorization.
    The algorithm is composed by two phase:
        - firstPhase: calculates a non-trivial factor of an integer n, starting from random point
        - secondPhase: calculates a non-trivial factor of an integer n, starting from a finite point
"""

from fractions import gcd

from Point import Point


class Ecm:
    """ This method """

    def __init__(self):
        pass

    @staticmethod
    def first_phase(p, q, n, curve, smooth):
        k = smooth.get_k()
        ell_pow = [p]
        k = bin(k)[2:]
        len_k = len(k)
        for i in range(1, len_k):
            res = Point.sum_points(ell_pow[i-1], ell_pow[i-1], curve, n)
            if res.get_inf() > 1:
                return gcd(res.get_inf(), n)
            ell_pow.append(res)

        res = Point(q.get_x(), q.get_y(), q.get_inf())
        for i in range(0, len_k):
            if k[len_k - 1 - i] == '1':
                res = Point.sum_points(ell_pow[i], res, curve, n)
                if res.get_inf() > 1:
                    return gcd(res.get_inf(), n)

        q.set_x(res.get_x())
        q.set_y(res.get_y())
        q.set_inf(1)
        return -1

    @staticmethod
    def second_phase(q, n, curve, smooth):
        primes = smooth.get_b2_prime()
        lim = smooth.get_increment()
        point_r = []
        k = 0
        for i in range(2, lim, 2):
            if i == 2:
                res = Point.sum_points(q, q, curve, n)
                if res.get_inf() > 1:
                    return gcd(res.get_inf(), n)
                point_r.append(res)
            else:
                res = Point.sum_points(point_r[0], point_r[k-1], curve, n)
                if res.get_inf() > 1:
                    return gcd(res.get_inf(), n)
                point_r.append(res)

            k = k + 1

        length = len(point_r)

        res = Point(q.get_x(), q.get_y(), 1)
        for k in range(0, primes[0]):
            res = Point.sum_points(q, res, curve, n)
            if res.get_inf() > 1:
                return gcd(res.get_inf(), n)

        for i in range(1, length):
                res = Point.sum_points(point_r[i - 1], res, curve, n)
                if res.get_inf() > 1:
                    return gcd(res.get_inf(), n)
        return -1