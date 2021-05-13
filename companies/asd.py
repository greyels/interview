a = [1,2,3]
b = [4,5,6,7]


def swap_lists_func(a, b):
    for i in a:
        b.append(i)
        print(len(b))
    del a[:]
    for _ in b:
        a.append(b.pop(0))

print('a =', a, id(a))
print('b =', b, id(b))
swap_lists(a, b)
print('a =', a, id(a))
print('b =', b, id(b))


def print_decor(fn):
    def wrap(*args, **kwargs):
        print(1)
        try:
            result = fn(*args, **kwargs)
        finally:
            print(2)
        return result
    return wrap

print({i**2: i for i in range(100)})
