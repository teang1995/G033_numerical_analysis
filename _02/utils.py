def iteration(func, num_iter):
    p = 1
    p_list = []
    for i in range(num_iter):
        p = func(p)
        print("{} - iteration : {}".format(i + 1, p))
        p_list.append(p)
    return p_list


def iteration_stop_by_error(func, error, p0):
    p_before = p0
    p_list = []
    i = 0
    while True:
        p_after = func(p_before)
        print("{}-iteration p{} : {}, p{} : {} ".format(i + 1, i, p_before, i + 1, p_after))
        if abs(p_after - p_before) < error:
            break
        p_before = p_after
        p_list.append(p_after)
        i += 1
    return p_list