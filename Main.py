from fractions import gcd

from Ecm import Ecm
from Point import Point
from Curve import Curve
from Smooth import Smooth
import sys
import random


def main():

    if len(sys.argv) != 3:
        print "Arguments error, passing 2 parameters"
        return

    # Initialization
    p1 = int(sys.argv[1])
    p2 = int(sys.argv[2])
    n = p1 * p2

    if p1 < p2:
        smooth = Smooth(p1)
    else:
        smooth = Smooth(p2)

    # Print points and curve
    print "Number to be factorized: " + n.__str__()
    print "B-smooth bound: " + smooth.get_b1().__str__()

    num = 0
    while True:
        print "Scelgo un punto a caso"
        P = Point(random.randint(0, n - 1), random.randint(0, n - 1), 1)
        Q = Point(P.get_x(), P.get_y(), 0)
        print "Creo la curva"
        curve = Curve(n, P)
        num += 1
        print "Curva numero: " + num.__str__()

        # Delta control
        g = gcd(curve.get_delta(), n)
        if g > 1:
            print "A non-trivial factor was found: " + g.__str__()
            return

        # Start the first phase
        print "Start first phase"
        res = Ecm.first_phase(P, Q, n, curve, smooth)
        # If the first phase fails
        if res == - 1:
            print "The first phase is failed...start second phase"
            res = Ecm.second_phase(Q, n, curve, smooth)
            if res > 0:
                print "A non-trivial factor was found in second phase: " + res.__str__()
                return
            else:
                print "The second phase is failed"

        # Else a non-trivial factor is calculated
        else:
            print "A non-trivial factor was found in first phase: " + res.__str__()
            return


if __name__ == "__main__":
    main()