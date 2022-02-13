'''
Function means set of statements which will perform a task.
1. function does not take arguments not returns any values(None)
2. function does not take arguments but returns some values
3. function takes arguments but no return value
4. function takes arguments and returns value
'''

# Example 1:
def myfun():              #declaration (statement) of function
    print("Hello")

myfun()                  # call the function/ invoking function
print("====================")

# Example 2:
def myfun1(name):
    print("Hello", name)

myfun1("Smith") # Hello Smith
print("====================")

# Example 3:
def cal(a,b):
    return (a+b)

sum = cal(10,20)
print(sum) # 30
print("====================")

# Example 4:
def func():
    return

print(func())  # None

def func1():
    i = 10

print(func1())  # None
print("====================")

# Example 5:
def calc(a,b):
    print(a+b)

calc(10,20)  # 30
# OR
def calc1(a,b):
    return (a+b)

print(calc1(10,20))  #30
print("====================")

# Example 6:


