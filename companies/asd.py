lst_a = [1, 2, 3]
lst_b = [4, 5, 6, 7]


def swap_lists_func(a, b):
    len_b = len(b)
    for i in a:
        b.append(i)
    del a[:]
    for i in range(len_b):
        a.append(b.pop(0))


print('a =', lst_a, id(lst_a))
print('b =', lst_b, id(lst_b))
swap_lists_func(lst_a, lst_b)
print('a =', lst_a, id(lst_a))
print('b =', lst_b, id(lst_b))


def print_decor(fn):
    def wrap(*args, **kwargs):
        print(1)
        try:
            result = fn(*args, **kwargs)
        finally:
            print(2)
        return result

    return wrap


print({i ** 2: i for i in range(100)})
