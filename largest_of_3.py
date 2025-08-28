print("Enter three integers to find the largest number.")
num1 = int(input("Integer 1: "))
num2 = int(input("Integer 2: "))
num3 = int(input("Integer 3: "))

if num1 > num2:
    if num1 > num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 > num3:
        largest = num2
    else:
        largest = num3

print("largest_of_3:", largest)