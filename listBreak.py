my_list = [1, 2, 3, 4, 5,
			6, 7, 8, 9]

# How many elements each
# list should have
n = 4

# using list comprehension
final = [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )]
print (final)
