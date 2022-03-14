# Python program to split a string and
# join it using different delimiter

def split_string(string):

	# Split the string based on space delimiter
	list_string = string.split(' ')
	
	return list_string



# Driver Function
if __name__ == '__main__':
	string = 'Welcome to python programming'
	
	# Splitting a string
	list_string = split_string(string)
	print(list_string)

	
