# Example1
def func(i, j):
    print(i, j)


func(10, 60)  # 10 60    positional arguments
func(j=90, i=10)  # 10 90 keyword arguments
print("================================")


# Example  2:
def func(i, j=10):
    print(i, j)


func(100, 200)  # 100 200
func(100)  # 100 10
print("================================")


# Example  3:
def greetings(name, greetings):
    print(greetings + ' ' + name)


greetings(name='John', greetings="Hello")  # Hello John    keyword arguments
greetings(greetings="Hello", name='John')  # Hello John    keyword arguments
print("================================")


# Example  4:
def my_func(a, b, c):
    print(a, b, c)


my_func(10, 20, 30)  # 10 20 30    positional arguments
my_func(a=10, b=20, c=30)  # 10 20 30    keyword arguments
my_func(a=10, c=30, b=20)  # 10 20 30  keyword arguments
my_func(10, 20, c=30)  # 10 20 30
my_func(10, b=20, c=30)  # 10 20 30
# my_func(10, b=20, 30)  #  SyntaxError: positional argument follows keyword argument (this is wrong
# as positional argument must appear before any key arguments)
# my_func(10, 30, b=20) # TypeError: my_func() got multiple values for argument 'b'   (logical error)
print("================================")


# Example  5:
def largest(a, b):
    if a > b:
        return a, b
    else:
        return b, a


print(largest(100, 200))  # (200, 100)
print(largest(20, 10))  # (20, 10)

res = largest(10, 60)
print(res)   # (60, 10)

print(type(res))  # <class 'tuple'>
