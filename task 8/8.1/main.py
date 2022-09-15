def g_func(x, res_c, method):
    result = method(x, res_c)
    for i in result:
        yield i


def on_res(x, res_c):
    result = []
    temp_res = x
    while len(result) < res_c:
        result.append(x * temp_res)
        temp_res += 1
    return result


gf = g_func(5, 10, on_res)

for i in gf:
    print(i)