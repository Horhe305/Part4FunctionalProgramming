""" Lambda Expression """
from functools import reduce
# lambda params: expression

num_list = [-1, 0, 1, 2, 3, 4]
# map(function, iterable)
print(list(map(lambda item: item + 1, num_list)))


# Exact same
def add_one(item):
    return item + 1


print(list(map(add_one, num_list)))

# Reduce example with lambda
# reduce(func, iterable, acc)

print(reduce(lambda acc, item: acc + item, num_list, 0))
