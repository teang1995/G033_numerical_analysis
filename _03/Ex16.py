from _03.methods import iteration_newtons_method
import math


def func(x):
    return 0.5 + pow(x, 2) / 4 - x * math.sin(x) - math.cos(2 * x) / 2


def func_derv(x):
    return x / 2 - math.sin(x) - x * math.cos(x) + math.sin(2 * x)


if __name__ == "__main__":
    print("************ pi / 2 ************")
    iteration_newtons_method(func, func_derv, math.pi / 2, pow(10, -5))
    print("************ 5 pi ************")
    iteration_newtons_method(func, func_derv, math.pi * 5, pow(10, -5))
    print("************ 10 pi ************")
    iteration_newtons_method(func, func_derv, math.pi * 10, pow(10, -5))