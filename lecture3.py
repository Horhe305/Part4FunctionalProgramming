""" Filter Function """


# help(filter)

# function
def only_even_nums(num_item):
    return num_item % 2 == 0


# numbers list
numbers_list = [1, 2, 3, 4, 5, 6]
# filter function
print(list(filter(only_even_nums, numbers_list)))


# --------- Example two ----------
# function
def name_cutter(name_item):
    return 'on' not in name_item


# users name
users_list = ['Tom', 'Brad', 'Bruce', 'Jason', 'Brandon']
# filter function
print(list(filter(name_cutter, users_list)))

