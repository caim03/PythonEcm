""" This class defines the b-smoothness bounds and some lists of prime """

import math


class Smooth:

    table = [(15, 2000, 25), (20, 11000, 90), (25, 50000, 300), (30, 250000, 700), (35, 1000000, 1800),
             (40, 3000000, 5100), (45, 11000000, 10600), (50, 43000000, 19300), (55, 110000000, 49000),
             (60, 260000000, 146000), (65, 850000000, 210000), (70, 2900000000, 340000)]

    def __init__(self, p):
        digits = math.floor(math.log(p, 10))
        for i in range(0, len(self.table)):
            if digits == self.table[i][0]:
                self.b1 = self.table[i][1]
                break
        self.b2 = self.b1 * 100
        self.b1_prime = self.smooth_prime(True)
        self.b2_prime = self.smooth_prime(False)
        self.expo = self.exp_list()
        self.max = self.calc_incr()
        self.k = 1
        length = len(self.b1_prime)

        for i in range(0, length):
            self.k = (self.b1_prime[i] ** self.expo[i]) * self.k

    def calc_incr(self):
        primes = self.get_b2_prime()
        length = len(primes)
        temp = 0

        for i in range(0, length - 1):
            if (primes[i + 1] - primes[i]) > temp:
                temp = primes[i + 1] - primes[i]

        return temp

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
            while self.b1_prime[i] ** m <= self.b1:
                m += 1
            exps.append(m - 1)

        return exps

    def get_k(self):
        return self.k

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

    def get_increment(self):
        return self.max

    def set_b1(self, b1):
        self.b1 = b1

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
    if b == 0:
        return 1, 0, a
    q, r = divmod(a, b)
    x, y, g = inverse(b, r)
    return y, x - q * y, g
