def geo_prog(start, a, length):
    count = 0
    while count < length:
        temp = (yield start)
        if temp == 'stop':
            print('Stop')
            break
        else:
            start *= a
            count += 1
    return


g = geo_prog(3, 4, 5)
for item in g:
    print(item)


def my_range(start=None, stop=None, step=None):
    if step is None:
        step = 1
    if not start is None and stop is None:
        start, stop = 0, start
    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step
    return


def prime_num(limit):
    for i in range(2, limit):
        x = 2
        while x < i:
            if i % x != 0:
                x += 1
            else:
                break
        else:
            yield i


list1 = [x ** 3 for x in range(2, 7)]
print(list1)
