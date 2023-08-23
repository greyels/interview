from functools import wraps


# count invocations decorator
def invoc_decor(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        wrapper.invoc += 1
        return fn(*args, **kwargs)
    wrapper.invoc = 0
    return wrapper


# cache decorator
def cache_decor(fn):
    @wraps(fn)
    def wrapper(*args):
        if args in wrapper.cache:
            print('taken from cache!')
            return wrapper.cache[args]
        result = fn(*args)
        wrapper.cache[args] = result
        print('cache isn\'t used!')
        return result
    wrapper.cache = {}
    return wrapper


# Test invocation count
calls_count = invoc_decor(print)
calls_count(1)
calls_count(1)
calls_count(1)
print(f'calls count = {calls_count.invoc}')

# Test cache decorator
cache_test = cache_decor(lambda x: x ** 2)
cache_test(2)
cache_test(3)
cache_test(2)
cache_test(3)
print(cache_test.cache)
