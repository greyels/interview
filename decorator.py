

# count invocations decorator
def invoc_decor(fn):
    def wrap(*args, **kwargs):
        wrap.invoc += 1
        return fn(*args, **kwargs)
    wrap.invoc = 0
    return wrap

calls_count = invoc_decor(print)
calls_count(1)
calls_count(1)
calls_count(1)
print(f'calls count = {calls_count.invoc}')