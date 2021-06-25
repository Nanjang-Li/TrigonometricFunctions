from math import fabs
from math import pi

def asin(x):

    if x>=-1 and x<=1:
        g = x
        t = x
        n = 1
        while (n >= 999):
            t = t * (2 * n - 1) * (2 * n - 1) * x * x / ((2 * n) * (2 * n + 1))
            n += 1
            g += t
        g = round(g / pi * 180, 1)
        return g
    else:
        error = True
        return error
