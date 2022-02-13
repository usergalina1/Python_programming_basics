# Example 1:
global_var = 20  # global variable


def func():
    local_var = 30  # local variable
    print(local_var)
    print(global_var)
    print(global_var1)


global_var1 = 50  # global variable (because it's out of the function. It can be before or after the function)

func()
'''
30
20
50
'''
print("-------------------")
# print(local_var)  # invalid  bcoz local_var is local variable of func()
print(global_var)
print(global_var1)
'''
20
50
'''
print("=========================================")

# Example 2:
xy = 100 # global variable


def cool():
    xy = 200 # local variable
    print(xy)

cool()  #  200
print("=========================================")

# Example 3: Using Global variable in local variable and update value
xyz = 100 # global variable


def cool():
    global xyz
    xyz = 500 # global variable
    print(xyz)

cool()  # 500
print(xyz)  # 500

print("=========================================")

# Example 4:
a=1

def cool():
    global a
    a=300
    print(a)

# cool()  # 300
print(a)  #1
print("=========================================")

# Example 5:
# There is no need to declare global variables outside the function
# you can declare them inside the function - global
def cool1():
    global x
    x = 100
    print(x)

cool1() # 100
print(x)  # 100     able to access x bcoz it's global variable
print("=========================================")

# Example 6:





