from _02.utils import iteration


def func_1(x):
    return pow(3 + x - 2 * pow(x, 2), 0.25)


def func_2(x):
    return pow((x + 3 - pow(x, 4)) / 2, 0.5)


def func_3(x):
    return pow((x + 3) / (pow(x, 2) + 2), 0.5)


def func_4(x):
    return (3 * pow(x, 4) + 2 * pow(x, 2) + 3) / (4 * pow(x, 3) + 4 * x - 1)


if __name__ == "__main__":
    iterations_results = []
    print("g1(x)")
    iterations_results.append(iteration(func_1, 4))
    print("*********************************")
    print("g2(x)")
    iterations_results.append(iteration(func_2, 4))
    print("*********************************")
    print("g3(x)")
    iterations_results.append(iteration(func_3, 4))
    print("*********************************")
    print("g4(x)")
    iterations_results.append(iteration(func_4, 4))
    print("*********************************")

    min_ = 100000
    min_index = 0
    for i, result in enumerate(iterations_results):
        if abs(result[3] - result[2]) < min_:
            min_ = abs(result[3] - result[2])
            min_index = i

    print("g{}(x) gives the best approximation to the solution".format(min_index + 1))
