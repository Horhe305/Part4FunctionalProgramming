""" Zip Function """
# even list
even_list = [2, 4, 6, 8, 10]
# odd list
odd_list = [1, 3, 5, 7, 9]
# zip function
# print(list(zip(even_list, odd_list)))
zipped_list = list(zip(even_list, odd_list))
print(zipped_list[1])

# even tuple
even_tuple = (2, 4, 6, 8, 10)
# odd tuple
odd_tuple = (1, 3, 5, 7, 9)
# zip function
print(tuple(zip(even_tuple, odd_tuple)))
