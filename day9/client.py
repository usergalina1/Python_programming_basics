'''
pack1 ==> module1 ==> display()
      ==> module2 ==> show()
'''

# Approach 1
import sys
sys.path.append("C:/Users/galin/PycharmProjects/pythonTraining/day9/pack1")

import module1 # don't pay attention, python doesn't recognize this
import module2 # don't pay attention, python doesn't recognize this

module1.display() # This is display function from module 1
module2.show() # This is show function from module 2
print("=================")

# Approach 2 # don't pay attention, python doesn't recognize these errors
from  module1 import *
from  module2 import *

display()
show()
'''
This is display function from module 1
This is show function from module 2
'''
print("=================")


