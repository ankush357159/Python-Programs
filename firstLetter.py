# Python Program get first character of string

# take input
string = input('Enter any string: ')

# get first character
first_char = ""
for i in range(0, 1):
    first_char = first_char + string[i]

# printing first character of string
print('First character:', first_char)