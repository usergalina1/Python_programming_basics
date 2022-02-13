'''
Package      Modules Classes   Methods
packageA ==> emp ==> Employee: displayemp()
packageB ==> stu==>  Student:  displaystu()
packageC ==>client
'''

# Approach 1
import sys
sys.path.append("C:/Users/galin/PycharmProjects/pythonTraining/day9/packageA")
sys.path.append("C:/Users/galin/PycharmProjects/pythonTraining/day9/packageB")

import emp
import stu

eobj = emp.Employee(11, "Ann", 10000)
eobj.displayemp()    # 11 Ann 10000

sobj = stu.Student(156,"John", 5)
sobj.displaystu()   # 156 John 5
print("=============================")

# Aproach 2
import sys
sys.path.append("C:/Users/galin/PycharmProjects/pythonTraining/day9/packageA")
sys.path.append("C:/Users/galin/PycharmProjects/pythonTraining/day9/packageB")

from emp import Employee
from stu import Student

eobj = Employee(11, "Ann", 10000)
eobj.displayemp()    # 11 Ann 10000

sobj = Student(156,"John", 5)
sobj.displaystu()   # 156 John 5
print("=============================")
