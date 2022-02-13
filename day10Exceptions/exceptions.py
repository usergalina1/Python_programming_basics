'''
Eception is an event which will cause program termination

'''
# Example1

print("this is starting point of programm...")
print("this is starting point of programm...")
print("this is starting point of programm...")
try:
    print(x)
except:
    print("Exception occured")
print("this is end of the program..")
print("this is end of the program..")
print("this is end of the program..")
'''
this is starting point of programm...
this is starting point of programm...
this is starting point of programm...
Exception occured
this is end of the program..
this is end of the program..
this is end of the program..
'''
print("====================")

# Example 2
print("this is starting point of programm...")
print("program is in progress")
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Exception occured.... handled...")
print("Program completed")
'''
this is starting point of programm...
program is in progress
Exception occured.... handled...
Program completed
'''
print("============================")

# Example 3 Multiple except blocks try, except else, finally
'''
:except --> executes only when exception occured
else --> executes only exceptions not occured
finally --> always executes
'''
try:
    num1, num2 = 10, 0
    result = num1 / num2
    print("result is:", result)
except ZeroDivisionError:
    print("Thrown ZeroDivisionError exception")
except SyntaxError:
    print(" Thrown Syntax error exception... ")
except:
    print("Exception handled...")
else:
    print("No exception occured...")
finally:
    print("always execute..")
'''
Thrown ZeroDivisionError exception
always execute..
'''
print("====================")


# Example 4: raising our own exceptions
def enterage(num):
    if num < 0:
        raise ValueError("Only integers are allowed")
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


print("checking number is even or odd by calling function")
num = -10
try:
    enterage(num)
except ValueError:
    print(" Value error exception occured and hadled...")
print("program completed")
'''
checking number is even or odd by calling function
 Value error exception occured and hadled...
program completed
'''
print("=====================")
