from _02.utils import iteration


def func_a(x):
    return (20 * x + 21 / pow(x, 2)) / 21


def func_b(x):
    return x - (pow(x, 3) - 21) / (3 * pow(x, 2))


def func_c(x):
    return x - (pow(x, 4) - 21 * x) / (pow(x, 2) - 21)


def func_d(x):
    return pow(21/x, 0.5)


if __name__ == "__main__":
    iterations_results = []
    print("g1(x)")
    iterations_results.append(iteration(func_a, 10))
    print("*********************************")
    print("g2(x)")
    iterations_results.append(iteration(func_b, 10))
    print("*********************************")
    print("g3(x)")
    iterations_results.append(iteration(func_c, 10))
    print("*********************************")
    print("g4(x)")
    iterations_results.append(iteration(func_d, 10))
    print("*********************************")

    min_ = 100000
    min_index = 0
    converge_list = []
    for i, result in enumerate(iterations_results):
        converge_list.append([i + 1, result[9] - result[8]])

    converge_list.sort(key = lambda x : abs(x[1]))
    print(converge_list)