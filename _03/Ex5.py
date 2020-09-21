from _03.methods import newtons_method
from _03.methods import iteration_newtons_method
import math


def func_1(x):
    return pow(x, 3) - 2 * pow(x, 2) - 5


def func_1_derv(x):
    return 3 * pow(x, 2) - 4 * x


def func_2(x):
    return pow(x, 3) + 3 * pow(x, 2) - 1


def func_2_derv(x):
    return  3 * pow(x, 2) + 6 * x


def func_3(x):
    return x - math.cos(x)


def func_3_derv(x):
    return 1 + math.sin(x)


def func_4(x):
    return x - 0.8 - 0.2 * math.sin(x)


def func_4_derv(x):
    return 1 - 0.2 * math.cos(x)


if __name__ == "__main__":
    print("************ 5 - a ************")
    iteration_newtons_method(func_1, func_1_derv, 2, pow(10, -4))
    print("************ 5 - b ************")
    iteration_newtons_method(func_2, func_2_derv, -2.5, pow(10, -4))
    print("************ 5 - c ************")
    iteration_newtons_method(func_3, func_3_derv, math.pi / 4.0, pow(10, -4))
    print("************ 5 - d ************")
    iteration_newtons_method(func_4, func_4_derv, math.pi / 4.0, pow(10, -4))