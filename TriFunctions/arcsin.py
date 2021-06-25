from math import fabs
from math import pi

def asin(x):
    '''
    :param x: 输入参数为数值
    :return g or error:输出为角度值或抛出异常
    
    '''

    if x>=-1 and x<=1:  #判断输入数值是否在定义域内
        g = x
        t = x
        n = 1
        while (n >= 999):  #采用泰勒级数展开进行计算逼近函数值
            t = t * (2 * n - 1) * (2 * n - 1) * x * x / ((2 * n) * (2 * n + 1))
            n += 1
            g += t
        g = round(g / pi * 180, 1)
        return g
    else:
        error = True  #实现异常处理，当输入超出定义域范围，返回异常error
        return error
