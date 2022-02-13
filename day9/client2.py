# Approach Importing modules from different packages

#Approach1
'''
pack1 ==> module1 ==> display()
pack1 ==> pack2 ==>module2==> show()
'''

import sys
sys.path.append("C:/Users/galin/PycharmProjects/pythonTraining/day9/package1")
sys.path.append("C:/Users/galin/PycharmProjects/pythonTraining/day9/package1/package2")
import module1
import module2

module1.display()  # This is display function from module 1
module2.show()  #This is show function from module 2
print("=======================")

# Approach 2
import sys
sys.path.append("C:/Users/galin/PycharmProjects/pythonTraining/day9/package1")
sys.path.append("C:/Users/galin/PycharmProjects/pythonTraining/day9/package1/package2")

from module1 import*
from module2 import*

display()
show()
'''
This is display function from module 1
This is show function from module 2
'''
