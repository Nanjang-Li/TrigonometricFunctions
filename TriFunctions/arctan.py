from math import pi
from math import fabs

def atan(x):
    """
    :param x: input tan value of angle
    :return:
    """
    if fabs(x) < 1:      # 输入值绝对值小于1时，采用泰勒级数展开
        g = x
        t = x
        n = 1
        while (n < 9999):
            t = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
            g += t
            n += 1
    else:               # 输入值绝对值大于1，用 pi/2 - atan(x)
        x = 1/x
        g = x
        t = x
        n = 1
        while (n < 9999):
            t = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
            g += t
            n += 1
        g = pi/2 - g
        
    if x >= 0:
        g = round(g / pi * 180, 2)
    
    elif x < 0:
        if g >= 0:
            g = round((g - pi) / pi * 180, 2)
        else :
            g = g + pi
            g = round((g - pi) / pi * 180, 2)
        
    return g

