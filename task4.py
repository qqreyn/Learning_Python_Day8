def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input("Enter number to check if its even or not: "))

print("is", num, "even:", is_even(num))