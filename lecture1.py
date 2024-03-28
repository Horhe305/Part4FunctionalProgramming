"""
Pure Functions
In Python, a pure function is a function that has no side effects
and provides the same output for the same set of inputs.
It doesn't alter any state or data outside its scope
and its execution relies solely on its input arguments.
"""


# PURE
def odd_numbers(even_list):
    odd_list = []
    for item in even_list:
        odd_list.append(item - 1)
    return odd_list


print(odd_numbers([2, 4, 6, 8, 10]))

# NOT PURE
odd_list1 = []


def odd_numbers1(even_list):
    for item in even_list:
        odd_list1.append(item - 1)
    return odd_list1


print(odd_numbers1([2, 4, 6, 8, 10]))
