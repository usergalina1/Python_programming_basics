'''
Inheritance - acquiring all the attributes(variables) and behavior(methods) from pne class to another class
class A --> a,b,c, m1(),m2(), --> A is parent of B class    (Base class/ Super class)
class B(A) --> x,y,z, m3(), --> B is parent of A class    (Sub class/ Derived class)

Objectives of inheritance:
1) Code re-usability
2) Avoid duplication

Types:
- single
- multi level
- heirarchy
- multiple
'''

#Example 1  Single inheritance
# class A:
#     def m1(self):
#         print("this is m1 method from class A")
#
# class B(A):
#     def m2(self):
#         print("this is m1 method from class B")
#
# bobj = B()
# bobj.m1()  #this is m1 method from class A
# bobj.m2()

#Example 2 Another single inheritance
# class A:
#     x,y = 10,20
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):
#     a,b = 100,200
#     def m2(self):
#         print(self.a - self.b)
#
# bobj = B()
# bobj.m1() # 30
# bobj.m2() #-100

#Example 3 Multi level inheritance
# class A:
#     x,y = 10,20
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):
#     a,b = 100,200
#     def m2(self):
#         print(self.a - self.b)
#
# class C(B):
#     i,j = 5,2
#     def m3(self):
#         print(self.i * self.j)
#
# cobj = C()
# cobj.m1() # 30
# cobj.m2()  # -100
# cobj.m3()  # 10

# #Example 4 heirarchy inheritance
# class A:
#     x,y = 10,20
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):
#     a,b = 100,200
#     def m2(self):
#         print(self.a - self.b)
#
# class C(A):
#     i,j = 5,2
#     def m3(self):
#         print(self.i * self.j)
#
# cobj = C()
# cobj.m1() # 30
# cobj.m3()  # 10
#
# bobj = B()
# bobj.m1() # 30
# bobj.m2() # -100

#Example 5 multiple inheritance
# class A:
#     x,y = 10,20
#     def m1(self):
#         print(self.x + self.y)
#
# class B:
#     a,b = 100,200
#     def m2(self):
#         print(self.a - self.b)
#
# class C(A, B):
#     i,j = 5,2
#     def m3(self):
#         print(self.i * self.j)
#
# cobj = C()
# cobj.m1() # 30
# cobj.m3()  # 10
# cobj.m2()  #-100

# Example 6: calling parnt class method using child class (super())
# class A:
#     def m1(self):
#         print("This is m1 method from class A")
#
# class B(A):
#     def m1(self):
#         print("This is m1 method from class B")  # Overriding concept
#         super().m1() # indirectly invoked parent class
#
# bobj = B()
# bobj.m1()
# Result:
# This is m1 method from class B
# This is m1 method from class A

# # Example 7:
# class A:
#     a,b, = 10,20
#
# class B(A):
#     i,j = 100,200
#     def m(self, x, y):
#         print(x+y)  # local variables
#         print(self.i +self.j) # class variables
#         print(self.a + self.b)  # class variables
#
# bobj = B()
# bobj.m(1000, 2000)
'''
Result:
3000
300
30
'''

# Example 8: overriding variables
# class Parent:
#     name = "Scott"
#
# class Child(Parent):
#     name = "John"   # overriding the variable value
#     def test(self):
#         print(super().name)
#
# cobj = Child()
# print(cobj.name) # John
# cobj.test()  # Scott

# Example 9: overriding methods
# class Bank:
#     def rateOfInterest(self):
#         return 0
#
# class XBank(Bank):
#     def rateOfInterest(self):
#         return 10
#
# class YBank(Bank):
#     def rateOfInterest(self):
#         return 12
#
# objx=XBank()
# print(objx.rateOfInterest()) # 10
#
# objy=YBank()
# print(objy.rateOfInterest()) # 12

'''
polymorphizm we can implement using overloading concept
'''

# Example 10(1): overloading (polymorphism)
class Human:
    def sayHello(self, name=None):
        if name is not None:
            print("Hello " + name)
        else:
            print("Hello")
h = Human()
h.sayHello("scott")  # Hello scott
h.sayHello() # Hello

# Example 11(2): overloading (polymorphism)
class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

calobj = Calculation()
calobj.add()  #0
calobj.add(10,20)  # 30
calobj.add(100,200, 300) # 600


