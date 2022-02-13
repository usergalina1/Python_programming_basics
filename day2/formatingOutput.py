# name='john'
# age=30
# sal = 5000.50
name, age, sal = 'john', 30, 500.50

# Approach 1
print(name)
print(age)
print(sal)
print(name, age, sal)
print(name, age)

# Approach 2
print("Name is:", name)
print("Age is:", age)
print("Sal is:", sal)
'''
Result:
Name is: john
Age is: 30
Sal is: 500.5
'''

# Approach 3
print("Name is:%s Age is:%d Salary is:%g" % (name, age, sal))

'''
Result:
Name is:john Age is:30 Salary is:500.5
'''

# Approach 4
print("Name is:{} Age is:{} Salary is:{}".format(name, age, sal))  #should be the same order of variables
'''
Result:
Name is:john Age is:30 Salary is:500.5
'''
