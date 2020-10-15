

def mygen():
    i = 0
    while True:
        yield i
        i += 1


for item in mygen():
    print(item)
