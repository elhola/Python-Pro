import time


def dec(count, file_name):
    def file_time(function):
        self_name = function.__name__

        def wrapper(argument):
            c = 0
            start = time.time()
            while c <= count:
                res = function(argument)
                c += 1
            res_t = time.time() - start
            file = open(str(file_name) + '.txt', 'w')
            file.write(f'{str(res_t)} sec for {count} times run function {self_name}')
            file.close()
            return res

        return wrapper

    return file_time


@dec(10000000, 'here')
def pow_3(n):
    return n ** 3


print(pow_3(10))
