from _03.methods import newtons_method
import math


def func(x):
    return -pow(x, 3) - math.cos(x)


def func_derv(x):
    return -3 * pow(x, 2) + math.sin(x)


if __name__ == "__main__":
    p = -1 #p0
    for i in range(2):
        p = newtons_method(p, func, func_derv)
        print("p{} is {}".format(i + 1, p))
