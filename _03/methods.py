def newtons_method(x, func, func_derv):
    return x - func(x)/func_derv(x)


def secant_method(func, x0, x1):
    return x0 - func(x0) * (x0 - x1) / (func(x0) - func(x1))


def iteration_newtons_method(func, func_derv, x, error):
    i = 0
    while True:
        p = newtons_method(x, func, func_derv)
        print("{}-iteration is {}".format(i + 1, p))
        if abs(p - x) < error:
            break
        x = p
        i += 1
    return p


