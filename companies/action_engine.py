a = [[None]] * 3
a[0][0] = 1
print(a)
# [[1], [1], [1]]

b = [[None] for i in range(3)]
b[0][0] = 1
print(b)
# [[1], [None], [None]]

c = ([1] for i in range(3))
c[0][0] = 1
print(c)
# TypeError: 'generator' object is not subscriptable

d = {i[0]: str(i) for i in b}
print(d[b[-1][-1]])
# "[None]"


# Mutable default argument
def my_fn(val, acc=[]):
    acc.append(val)
    return acc

my_fn(1)
# [1]
my_fn(2)
# [1, 2]
my_fn(3, [1, 2])
# [1, 2, 3]


# --- Присваивание лямбда-функции!!!
my_fn = lambda *args, **kwargs: print(str(args), str(kwargs))
my_fn("first", "second", "third", forth="forth", fifth="fifth")
# "('first', 'second', 'third')" "{'forth': 'forth', 'fifth': 'fifth'}"


# Id	Name			ReferredBy
# 1	John Doe		NULL
# 2	Jane Smith		NULL
# 3	Anne Jenkins    2
# 4	Eric Branford	NULL
# 5	Pat Richards	1
# 6	Alice Barnes	2


# SELECT Name FROM Customers WHERE ReferredBy <> 2;
# 5	Pat Richards	1

# SELECT name, COUNT(email) 
# FROM users
# GROUP BY email
# WHERE COUNT(email) > 1 (issue! Should be HAVING)


# Pandas

#        Name      City  Items
# 0     Alice   Seattle      1
# 1     Alice  Portland      7
# 2   Charlie  New York      6
# 3       Bob  New York      0
# 4       Bob   Seattle      7
# 5       Bob  Portland      2
# 6   Charlie  Portland      1
# 7   Charlie   Seattle      2
# 8     Alice  New York      7
# 9     Alice  New York      6
# 10    Alice   Seattle      4
# 11  Charlie  New York      2
# 12      Bob  Portland      0
# 13      Bob   Seattle      1
# 14  Charlie  Portland      2
# 15    Alice  Portland      3
# 16      Bob  New York      1
# 17  Charlie   Seattle      4

# gb1 = df.groupby(["Name", "City"]).sum()

#                   Items
# Name    City
# Alice   New York     13
#         Portland     10
#         Seattle       5
# Bob     New York      1
#         Portland      2
#         Seattle       8
# Charlie New York      8
#         Portland      3
#         Seattle       6

# gb1.loc["Alice", "Seattle"]["Items"]

# gb1.reset_index()

#       Name      City  Items
# 0    Alice  New York     13
# 1    Alice  Portland     10
# 2    Alice   Seattle      5
# 3      Bob  New York      1
# 4      Bob  Portland      2
# 5      Bob   Seattle      8
# 6  Charlie  New York      8
# 7  Charlie  Portland      3
# 8  Charlie   Seattle      6