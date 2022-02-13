'''
1) Check the given number is Positive or negative
2) Check the largest of 2 numbers
3) Check the largest of 3 numbers
4) Print week number if you provide weekname as input
'''

# 1)Check the given number is Positive or negative

x = -15
if x < 0:
    print("negative")
else:
    print("positive")

# 2) Check the largest of 2 numbers
a = 15
b = 800
print("a greater b") if a > b else print("b greater a")

# 3) Check the largest of 3 numbers
a = 15
b = 800
c = -90
if a > b and a > c:
    print("a is the largest")
elif b > a and b > c:
    print("b is the largest")
else:
    print("c is the largest")

# 4) Print week number if you provide weekname as input

weekname = "Friday"

if weekname == "Sunday":
    print(1)
elif weekname == "Monday":
    print(2)
elif weekname == "Tuesday":
    print(3)
elif weekname == "Wednesday":
    print(4)
elif weekname == "Thursday":
    print(5)
elif weekname == "Friday":
    print(6)
elif weekname == "Saturday":
    print(7)
