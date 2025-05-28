num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))

num = int(input("Enter the number"))
if num % 3 == 0 and num % 5 == 0:
    print("{0} is divisible by both 3 and 5".format(num))
elif num % 3 == 0:
    print("{0} is divisible by both 3".format(num))
elif num % 5 == 0:
    print("{0} is divisible by both 5".format(num))
else:
    print("{} is not divisible by both 3 and 5".format(num))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number between", num1, ",", num2, "and", num3, "is", largest)

year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

x = 5
y = 10
print("Before swapping:")
print(x)
print(y)
temp = x
x = y
y = temp
print("After swapping:")
print(x)
print(y)


# def rotate(l, order):
#     for i in range(0, order):
#         j = len(l) - 1
#         while j > 0:
#             temp = l[j]
#             l[j] = l[j - 1]
#             l[j - 1] = temp
#             j = j - 1
#             print(i, "rotation", l)


# l = [1, 2, 3, 4, 5]
# rotate(l, 3)

import math


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print("The value of dx is", dx)
    print("The value of dy is", dy)
    d = math.sqrt((dx**2 + dy**2))
    print("Distance between two points is", d)


distance(0, 0, 3, 3)
