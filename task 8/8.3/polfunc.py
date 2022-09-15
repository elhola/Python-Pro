def sum_seq(seq_list, some_func):
    x = 0
    for i in seq_list:
        y = (some_func(i))
        x += y
    return x


def pow_2(i):
    return i ** 2


l = (1, 2, 3, 4, 5)

print(sum_seq(l, pow_2))
