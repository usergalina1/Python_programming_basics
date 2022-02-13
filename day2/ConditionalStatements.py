# conditional statements
# if  if..else   elif

# Example : Print a person is eligible for vote or not
#          age>=18
age = 15
if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")

# Example 2:
if True:
    print("true condition")
else:
    print("false condition")

# Example 3:
if 0:
    print("one")
else:
    print("not one")

# Example 4: Find a number is even/odd
num = 15
if num % 2 == 0:
    print("Given number is even")
else:
    print("Given number is odd")

# Example 5: if else in single line (ternary operator)
num = 10
print("Even number") if num % 2 == 0 else print("odd number")
'''
Result:Even number
'''

# Example 6: if else - Multiple statements in single line (ternary operator)
num = 20
{print("hello"), print("python")} if num >= 10 else {print("hi"), print("java")}
'''
Result:
hello
python
'''

# Example 7: Multiple conditions using elif
weekno = 7

if weekno == 1:
    print("Sunday")
elif weekno ==2:
    print("Monday")
elif weekno ==3:
    print("Tuesday")
elif weekno ==4:
    print("Wednesday")
elif weekno ==5:
    print("Thursday")
elif weekno ==6:
    print("Friday")
elif weekno ==7:
    print("Saturday")
else:
    print("Invalid week number")


