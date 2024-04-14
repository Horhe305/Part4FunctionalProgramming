""" Set and Dictionary Comprehension """
# first set
first_set = {10, 12, 14, 16}

# set comprehension
second_set = {num for num in first_set}
print(second_set)

# example 2
long_set = {num for num in range(0, 100)}
print(long_set)

# Dictionary
my_dict = {
    'one': 1,
    'two': 2,
    'three': 3
}

# my_dict2 = {key: value for key, value in my_dict.items()}
# my_dict2 = {key: value + 1 for key, value in my_dict.items()}
my_dict2 = {key: value for key, value in my_dict.items() if value % 2 == 0}
print(my_dict2)
