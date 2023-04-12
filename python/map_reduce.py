# https://neurohive.io/ru/tutorial/mapreduce/
from functools import reduce

# find the longest string in list of strings
def find_longest_string(list_of_strings):
    longest_string = None
    longest_string_len = 0
    for s in list_of_strings:
        if len(s) > longest_string_len:
            longest_string_len = len(s)
            longest_string = s
    return longest_string


list_of_strings = ["123", "sds", "erwer"]

# step 1:
list_of_string_lens = [len(s) for s in list_of_strings]
list_of_string_lens = zip(list_of_strings, list_of_string_lens)
#step 2:
max_len = max(list_of_string_lens, key=lambda t: t[1])

# simple mapper and reducer
mapper = len
def reducer(p, c):
    if p[1] > c[1]:
        return p
    return c

#step 1
mapped = map(mapper, list_of_strings)
mapped = zip(list_of_strings, mapped)
#step 2:
reduced = reduce(reducer, mapped)
print(reduced)

data_chunks = chunkify(list_of_strings, number_of_chunks=30)
#step 1:
reduced_all = []
for chunk in data_chunks:
    mapped_chunk = map(mapper, chunk)
    mapped_chunk = zip(chunk, mapped_chunk)
    reduced_chunk = reduce(reducer, mapped_chunk)
    reduced_all.append(reduced_chunk)
#step 2:
reduced = reduce(reducer, reduced_all)
print(reduced)

# with multiprocessing
from multiprocessing import Pool
pool = Pool(8)
data_chunks = chunkify(large_list_of_strings, number_of_chunks=8)
#step 1:
mapped = pool.map(mapper, data_chunks)
#step 2:
reduced = reduce(reducer, mapped)
print(reduced)
