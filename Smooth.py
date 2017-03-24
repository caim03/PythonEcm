""" This class defines the b-smoothness bounds and some lists of prime """

import math
from fractions import gcd


class Smooth:
    def __init__(self):
        self.b1 = 2500
        self.b2 = self.b1 * 100
        self.b1_prime = self.smooth_prime(True)
        self.b2_prime = self.smooth_prime(False)
        self.expo = self.exp_list()

    def smooth_prime(self, b):
        primes = []
        if b:
            for i in range(2, self.b1 + 1):
                if is_prime(i):
                    primes.append(i)

            return primes

        else:
            for i in range(self.b1, self.b2 + 1):
                if is_prime(i):
                    primes.append(i)

            return primes

    def exp_list(self):
        exps = []
        lenght = len(self.b1_prime)

        for i in range(0, lenght):
            m = 1
            while math.pow(self.b1_prime[i], m) <= self.b1:
                m += 1
            exps.append(m - 1)

        return exps

    def get_b1(self):
        return self.b1

    def get_b2(self):
        return self.b2

    def get_b1_prime(self):
        return self.b1_prime

    def get_b2_prime(self):
        return self.b2_prime

    def get_expo(self):
        return self.expo

    def to_string(self):
        print "B1 bound: " + self.b1.__str__()
        print "B2 bound: " + self.b2.__str__()
        print "B1 primes: " + self.b1_prime.__str__()
        print "B2 primes: " + self.b2_prime.__str__()
        print "Exponentials: " + self.expo.__str__()


def is_prime(n):
    if n == 1 or n == 2:
        return True

    if n % 2 == 0 and n > 2:
        return False

    sqrt = int(math.sqrt(n))
    for i in range(3, sqrt + 1, 2):
        if n % i == 0:
            return False
    return True


def inverse(a, b):
    x0 = 0
    x1 = 1

    a = a % b
    if a < b:
        a = b + a

    if gcd(a, b) != 1:
        return -1

    while a > 1:
        q = a / b
        t = b
        b = a % b
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t

    if x1 < 0:
        x1 = x0 + b

    return x1