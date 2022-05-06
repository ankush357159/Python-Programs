# Python program to do basic arithmetic operations

# Function to add two numbers
def add(a, b):
    return a + b

# Function to substract two numbers
def substract(a, b):
    return a - b

# Funciton to multipy two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    return a / b


print("Selection operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")


while True:
    choice = input("Enter choice (1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", substract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))


        # Check if user wants another calculation
        # Break the while loop if answer is no

        next_calculation = input("Lets do the next calculation?(yes/no): ")

        if next_calculation in ("no","N","n","NO","No","nO"):
            break

    else:
        print("Invalid Input")



