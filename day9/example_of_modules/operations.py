# Modules & Packages
'''
Module --> collection of functions, classes(variables+methods)
'''

#1 option
from day9.example_of_modules import calculator

calculator.add(100, 200) #300
calculator.mul(10, 20)  #200
print("========================")

# 2 Approach
from day9.example_of_modules.calculator import add,mul

add(10,20) #30
mul(100,200) #20000
print("========================")

# 3 Approach
from day9.example_of_modules.calculator import *

add(10,20) #30
mul(100,200) #20000
print("========================")