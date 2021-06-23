from math import fabs
from math import pi


def sin(x):
    x = x / 180 * pi
    g = 0
    t = x
    n = 1
    while (fabs(t) >= 1e-15):
        g += t
        n += 1
        t = -t * x * x / (2 * n - 1) / (2 * n - 2)
    return round(g, 3)


ans = sin(60)
print(ans)


