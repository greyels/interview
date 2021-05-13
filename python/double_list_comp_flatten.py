lst1 = [1, 2, 3, 4]
lst2 = [10, 20, 30, 40]


def double_list(list1, list2):
    res = []
    for i in list1:
        for j in list2:
            res.append(i * j)
    return res


print("Via function:")
print(double_list(lst1, lst2))

double_list_comp = [i * j for i in lst1 for j in lst2]

print("Via list comprehension:")
print(double_list_comp)

# option 2
book = [("book", "chapter"), ("Tolkien", "Hobbit")]

flatten = lambda book: [item for sublist in book for item in sublist]
print("Via lambda function (flatten):")
print(flatten(book))
