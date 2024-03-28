""" Map() Function """


# help(map)
def odd_numbers(list_item):
    return list_item - 1


even_list = [2, 4, 6, 8, 10]
print(list(map(odd_numbers, even_list)))


# Example 2
def user_names(user_item):
    return user_item.upper()


user_list = ['andy', 'tom', 'stipe']
print(list(map(user_names, user_list)))
