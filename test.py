from math import cos


def func(x):
    return pow(x, 0.5) - cos(x)


def sign(x):
    return x / abs(x)


def Bisection(a, b):
    p = (a + b) / 2.0
    if sign(func(a)) == sign(func(b)):
        a = p
    else:
        b = p
    return a, b


def isEnd(p1, p2, tol):
    return abs(p1 - p2) >= tol


def printMsg(a, b, i):
    print("{} - iteration : f(x) has a root in interval [{}, {}]".format(i, a, b))


if __name__ == "__main__":
    a = 0
    b = 1
    i = 1
    tol = pow(10, -4)
    flag = True
    while i <= 3:
        a, b = Bisection(a, b)
        flag = isEnd(a, b, tol)
        printMsg(a, b, i)
        i += 1