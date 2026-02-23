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

print("Calculator select operation (1-4): ")
print("1. Sum")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = int(input("Which operation you choose: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(calculator(num1, num2, operation))

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