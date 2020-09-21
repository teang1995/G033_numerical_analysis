from _02.utils import iteration_stop_by_error
import math


def func_1(x):
    return (2 - math.exp(x) + pow(x, 2)) / 3


def func_2(x):
    return(5 / pow(x, 2)) + 2


def func_3(x):
    return pow(math.exp(x)/3, 0.5)


if __name__ == "__main__":
    print("11 - 1")
    p_list = iteration_stop_by_error(func_1, pow(10, -5), 0.5)
    print("*********************************")
    print("11 - 2")
    p_list = iteration_stop_by_error(func_2, pow(10, -5), 3)
    print("*********************************")
    print("11 - 3")
    p_list = iteration_stop_by_error(func_3, pow(10, -5), 0.5)
    print("*********************************")
