'''
class - collection of variables(attributes) & methods(behavior)
A class  id blue print
Logical entity
Does not occupy space in the memory

object - is an instance of class
Physical entity
Occupy certain amount space in the memory

For one class, we can create multiple objects
Objects are independent

Functions Vs Methods
Function - we can create without class
Method - creates inside the class

2 types of methods we can define within the class
1) instance method (we can call only through object)
2) static method(we can directly call using class)
'''
'''
OOP concept:
class
object -> methods, static methods, constructor
inheritance -> types, overloading, super
polymorphism
'''

# Example1
# class MyClass:
#     def myFunc(self):
#         pass
#
#     def display(self):
#         print("John")
#
# mc1 = MyClass()
# mc1.myFunc()
# mc1.display()
#
# mc2 = MyClass()
# mc3 = MyClass()

# Example2
# class MyClass:
#     def m1(self):
#         print("this is instance method")
#
#     @staticmethod  # annotation
#     def m2(self, num):
#         print(self, num)
#
#
# mc = MyClass()
# mc.m1()
# mc.m2(100, 200)  # 100 200
#
# MyClass.m2(10, 20) # 10 20   here calling static method directly using class not through object

# Example3  Class variable
'''
Global variables
Class variables
Local variables
'''


# class MyClass:
#     a, b = 10, 20  # class variables, because they are created inside the class
#
#     def add(self):
#         print(self.a + self.b)
#
#     def mul(self):
#         print(self.a * self.b)
#
#
# mc = MyClass()
# mc.add()
# mc.mul()

# # Example4  Class variable
# i, j = 15, 25  # global variables
# class MyClass:
#     c, d = 10, 20  # class variables
#     def add(self, x,y):
#         print(x + y)  # x, y are local variables
#         print(self.c + self.d)  # class variables
#         print(i+j)  # global variables
#
# mc = MyClass()
# mc.add(100,200)
'''
Result:
300
30
40
'''

# Example5
# c,d = 15, 25  # global variables
# class MyClass:
#     c, d = 10, 20  # class variables
#     def add(self, c,d):
#         print(c + d)  # x, y are local variables
#         print(self.c + self.d)  # class variables
#         print(globals()['c']+globals()['d'])  # global variables
#
# mc = MyClass()
# mc.add(100,200)
'''
Result:
300
30
40
'''

#Example 6 One class can have multiple objects
# class MyClass:
#     def display(self,name):
#         print("this is  display method...")
#         print(name)
#
# obj1=MyClass()
# obj1.display("John")
#
# obj2=MyClass()
# obj2.display("Scott")

#Example 7 Constractor
'''
Method: give any name
        return the value/s
        method can take atguments/parameters
        we have to use an object to invoke/call the method
        
Constructor - name is fixed       def  __init__(self):
              will not return any value
              can take atguments/parameters
              will be called at the time of object creation itself
'''
# class MyClass:
#     def __init__(self):       #default constractor
#        print("this is constructor..")
#
#     def m1(self):
#         print("hello")
#     def m2(self, x, y):
#         return (x+y)
#
# mc=MyClass()  #invoke constructor automatically
# mc.m1()      #method we have call explicitly by using object
# print(mc.m2(10,20))  # 30

#Example 8

# class MyClass:
#     name = "John"
#     def __init__(self, name):   #parametrized constructor
#         print(name)
#         print(self.name)
# mc = MyClass("David")  # passing parameter to the constractor

# #Example 9
# '''
# Requirements: Employee
#               constractor: eid, ename, sal
#               display(): print eid, ename, sa
# '''
# class Empl:
#     def __init__(self, eid, ename, sal):
#         self.eid = eid
#         self.ename = ename
#         self.sal = sal
#
#     def display(self):
#         print(self.eid, self.ename, self.sal )
#
# emp = Empl(2, "John", 15000)
# emp.display()   # 2 John 15000
#
# emp1 = Empl(1, "Anna", 10000)
# emp1.display()   # 1 Anna 10000

#Example 10
'''
Requirements: Employee
              constractor: eid, ename, sal
              display(): print eid, ename, sa
'''
class Empl:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def __str__(self):   #cannot call numbers, it can only call strings
        return (self.ename)

emp = Empl(2, "John", 15000)
print(emp)  # John
