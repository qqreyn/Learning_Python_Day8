def greet(name):
    return name

def sum(num1, num2):
    return num1 + num2

def calculator(num1, num2, operation):
    if operation == 1:
        print(num1,"+", num2, "=", end=" ")
        return num1 + num2
    elif operation == 2:
        print(num1,"-", num2, "=", end=" ")
        return num1 - num2
    elif operation == 3:
        print(num1,"*", num2, "=", end=" ")
        return num1 * num2
    elif operation == 4:
        print(num1,"/", num2, "=", end=" ")
        return num1 / num2
    else:
        print("Incorrect operation")

def is_even(num1):
    if num1 % 2 == 0:
        return True
    else:
        return False

def power_calculation(num, exponent):
    return num ** exponent

print("Welcome to Math Program")
name = input("Enter your name: ")
print("Hello", greet(name), "nice to meet you!")

while True:
    print("What do you want to do?")
    print("1. Add two numbers")
    print("2. Use calculator")
    print("3. Check if number is even")
    print("4. Power calculation")
    print("5. Exit")
    
    choice = int(input("Pick option (1-5): "))

    if choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Sum of", num1, "and", num2, "is", sum(num1, num2))
    elif choice == 2:
        print("Calculator select operation (1-4)")
        print("1. Sum")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = int(input("Select operation (1-4): "))
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if operation == 1:
                oper = "Sum"
        elif operation == 2:
                oper = "Subtraction"
        elif operation == 3:
                oper = "Multiplication"
        elif operation == 4:
                oper = "Division"

        print("Operation:", oper)
        print("Number 1:", num1)
        print("Number 2:", num2)
        print(calculator(num1, num2, operation))

    elif choice == 3:
        num1 = int(input("Enter number to check if its even or not: "))
        print("Is", num1, "even:", is_even(num1))
    elif choice == 4:
        num1 = int(input("Enter number to be exponentiated: "))
        power = int(input("Enter what power to use: "))
        print(num1, "^", power, "is", power_calculation(num1, power))

    elif choice == 5:
        print("Goodbye", greet(name))
        break
    else:
        print("Incorrect option")
