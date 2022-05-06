# Python program to calculate factorial of a number

from math import factorial


def numberFactorial(num):
    factorial = 1
    for i in range(1, num +1):
        factorial = factorial * i
    return factorial


number = int(input("Enter any integer: "))

if number < 0:
    print("Factorial of a number can not be determined for negative numbers")

elif number == 0:
    print("Factorial of a number is 1")

else:
    fact = numberFactorial(number)

    print("Factorial of a {0} is: ".format(number), fact)    

print("Factorial of number calculated by python inbuild function: ",factorial(number))