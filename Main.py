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
    n = int(sys.argv[1]) * int(sys.argv[2])
    P = Point(random.randint(0, n - 1), random.randint(0, n - 1))
    Q = Point(P.get_x(), P.get_y())
    curve = Curve(n, P)

    # Print points and curve
    """print "Number to be factorized: " + n.__str__()
    P.to_string()
    Q.to_string()
    curve.to_string()
    smooth.to_string()"""

    # Delta control
    if (curve.get_delta() % n) == 0:
        print "This is not an elliptic curve on Z" + n
        return

    # Start the first phase
    res = Ecm.first_phase(P, Q, n, curve)

    # If the first phase fails
    if res < 0:
        print "The first phase is failed...start second phase"

    # Else a non-trivial factor is calculated
    else:
        print "A non-trivial factor was found: " + res.__str__()


if __name__ == "__main__":
    main()
