# count invocations decorator
def invoc_decor(fn):
    def wrap(*args, **kwargs):
        wrap.invoc += 1
        return fn(*args, **kwargs)
    wrap.invoc = 0
    return wrap

# cache decorator
def cache_decor(fn):
    def wrap(*args):
        if args in wrap.cache:
            print('taken from cache!')
            return wrap.cache[args]
        result = fn(*args)
        wrap.cache[args] = result
        print('cache isn\'t used!')
        return result
    wrap.cache = {}
    return wrap



calls_count = invoc_decor(print)
calls_count(1)
calls_count(1)
calls_count(1)
print(f'calls count = {calls_count.invoc}')

cache_test = cache_decor(lambda x: x**2)
cache_test(2)
cache_test(3)
cache_test(2)
cache_test(3)
print(cache_test.cache)