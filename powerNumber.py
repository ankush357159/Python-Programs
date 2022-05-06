# power = int(input("Enter the power to base 2: "))

# # result = list(map(lambda x: 2 ** x, range(power)))
# result = lambda x: 2**x

# print(result)

from functools import partial


num = 10
for i in range(-1, num):
    print(i)