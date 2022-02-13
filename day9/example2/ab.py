# Approach 1 import moduleName
from day9.example2 import a
import b

obj = a.Animal()
obj.display()

obj2 =b.Bird()
obj2.display()
'''
I like cow
I like parrot
'''
print("=======")

# Approach 2 from moduleName import functions, classes
from day9.example2.a import Animal
from b import Bird

obj1 = Animal()
obj1.display()

obj2 =Bird()
obj2.display()
'''
I like cow
I like parrot
'''
print("====================")

