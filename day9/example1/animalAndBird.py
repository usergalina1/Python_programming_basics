# Approach 1
'''
How to create a module
How to call the functions from one module to another module...
'''
from day9.example1 import animal, bird

animal.fly()
animal.color()

bird.fly()
bird.color()
'''
Animal can't fly
Animal is black
Bird can fly
Bird is green
'''
print("==================")

# Approach 2
'''
Same functions in two modules
'''
from day9.example1.animal import *
fly()
color()

from day9.example1.bird import *
fly()
color()
'''
Animal can't fly
Animal is black
Bird can fly
Bird is green
'''