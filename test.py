converters = [
    dict(g1="sds", g2="qeqwe"),
    dict(g2="sddfsdf"),
    dict(g1="shhjhj")
]

print([c["g1"] for c in converters if c.get("g1")])
print("------------------")
# print([c.get("g1") for c in converters])
print(*converters)
print([x for x in converters])
