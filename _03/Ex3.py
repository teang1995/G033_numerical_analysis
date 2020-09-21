from _03.methods import secant_method


def func(x):
    return pow(x, 2) - 6


if __name__ == "__main__":
    print("************ Secant Method ************")
    p0 = 3
    p1 = 2
    for i in range(2):
        p = secant_method(func, p1, p0)
        print("{}-iteration is {}".format(i + 1, p))
        p0 = p1
        p1 = p
    print(abs(p - pow(6, 0.5)))
    print("************ False position Method ************")
    p0 = 3
    p1 = 2
    for i in range(2):
        p = secant_method(func, p1, p0)
        print("{}-iteration is {}".format(i + 1, p))
        if p0 * p < 0:
            p0 = p1
            p1 = p
        else:
            p1 = p
    print(abs(p - pow(6, 0.5)))

