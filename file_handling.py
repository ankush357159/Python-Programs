my_file = open("text.txt", "w+")
#print(my_file.read())
#print(my_file.readline(2))
#print(my_file.readline())
#print(my_file.readlines())
#print(my_file)
#line_number = 4
#current_line = 1
#for line in my_file:
#		if (current_line == line_number):
#			print(line)
#			break

#		current_line += 1

#my_file.write("This is new lines added to file")
#my_file.write("This is line 1\n")
#my_file.write("This is line 2\n")
#fruits = ["apples\n", "mangoes\n", "cherries\n", "Grapes\n"]
#my_file.writelines(fruits)

#my_file.write("Guava")
#my_file.write("Another new text")
#my_file.write("Yet another new text")
#my_file.flush()
#n = input("Press any key to continue")
#my_file.write("Go to next counter")
#my_file.close()
myfile = open("text.txt")
line1 = myfile.readline()
print("Length of line is : ", len(line1))

line1 = line1.rstrip('\n')
print("Length of line is: ", len(line1))

line2 = myfile.readline()
print("Length of line is : ", len(line2))

line2 = line2.lstrip()
print("Length of line is : ", len(line2))
















