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
    P = Point(random.randint(0, n - 1), random.randint(0, n - 1))
    Q = Point(P.get_x(), P.get_y())
    curve = Curve(n, P)
    if p1 < p2:
        smooth = Smooth(p1)
    else:
        smooth = Smooth(p2)

    # Print points and curve
    print "Number to be factorized: " + n.__str__()
    P.to_string()
    Q.to_string()
    curve.to_string()

    # Delta control
    if (curve.get_delta() % n) == 0:
        print "This is not an elliptic curve on Z" + n.__str__()
        return

    # Start the first phase
    res = Ecm.first_phase(P, Q, n, curve, smooth)

    # If the first phase fails
    if res < 0:
        print "The first phase is failed...start second phase"
        res = Ecm.second_phase(Q, n, curve, smooth)
        if res > 0:
            print "A non-trivial factor was found in second phase: " + res.__str__()
        else:
            print "The second phase is failed"

    # Else a non-trivial factor is calculated
    else:
        print "A non-trivial factor was found in first phase: " + res.__str__()


if __name__ == "__main__":
    main()