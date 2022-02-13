# Example1:  how to create a list
'''
A list is a collectiion which is ordered and changeable
In Python lists are written with square brackets []
List is mutable
'''

myList1 = [10, 20, 30, 40, 50]
myList2 = ["apple", "banana", "cherry"]
myList3 = ["apple", 10, "banana", 30, "cherry"]
myList = list()  # empty list

print(myList1)  # [10, 20, 30, 40, 50]
print(myList2)  # ['apple', 'banana', 'cherry']
print(myList3)  # ['apple', 10, 'banana', 30, 'cherry']
print(myList)  # []
print("=========================")

# Example2: Accessing items from the list
myList4 = ["apple", "banana", "cherry", "orange"]
print(myList4[0])  # apple
print(myList4[2])  # cherry
print(myList4[-1])  # orange (start from the last one)
print(myList4[-2])  # cherry
print("=========================")

# Example3: Range of indexes
newList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(newList[2:5])  # ['cherry', 'orange', 'kiwi']
print(newList[-4:-1])  # ['orange', 'kiwi', 'melon']
print("=========================")

# Example4: change item values
myList5 = ["apple", "banana", "cherry"]
print(myList5)  # ['apple', 'banana', 'cherry']
myList5[0] = "orange"
print(myList5)  # ['orange', 'banana', 'cherry']
print("=========================")

# Example5: read the list items using loop
myList6 = ["apple", "banana", "cherry"]
for i in myList6:
    print(i)
'''
apple
banana
cherry
'''
print("=========================")

# Example6: check if the item is exist in the list or not
myList7 = ["apple", "banana", "cherry"]
if "apple" in myList7:
    print("yes, apple is present")
else:
    print("no apple is not present")
print("=========================")

# Example7: List length (counting number of items in a list)
myList8 = ["apple", "banana", "cherry"]
print(len(myList8))  # 3
print("=========================")

# Example8: Add items append()  insert()
myList9 = ["apple", "banana", "cherry"]
myList9.append("orange")  # adding new item at the end of the list
print(myList9)  # ['apple', 'banana', 'cherry', 'orange']

myList9.insert(3, "kiwi")  # adding item some where in the middle of the list based on the index
print(myList9)
print("=========================")

# Example 9: Remove item from the list
# pop()
myList10 = ["apple", "banana", "cherry"]
myList10.pop(0)  # here we should specify index not the value
print(myList10)  # ['banana', 'cherry']

# del
myList11 = ["apple", "banana", "cherry"]
del myList11[2]  # del command removes single item based on the index
print(myList11)  # ['apple', 'banana']

# clear
myList12 = ["apple", "banana", "cherry"]
myList12.clear()
print(myList12)  # []
print("=========================")

# Example 10: copy list
myList13 = ["apple", "banana", "cherry"]
# list()
myNewList13 = list(myList13)
print(myList13)
print(myNewList13)
'''
['apple', 'banana', 'cherry']
['apple', 'banana', 'cherry']
'''

# copy()
myNewestList13 = myList13.copy()
print(myNewestList13)  # ['apple', 'banana', 'cherry']
print("=========================")

# Example 11: combine/join lists
# using + operator
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3, ]
list3 = list1 + list2
print(list3)  # ['a', 'b', 'c', 1, 2, 3]

# using looping statement
l1 = ['a', 'b', 'c', "d"]
l2 = [1, 2, 3, 4]

for i in l2:
    l1.append(i)
print(l1)  # ['a', 'b', 'c', 'd', 1, 2, 3, 4]

# extend()
l3 = ['a', 'b', 'c', "d", "e"]
l4 = [1, 2, 3, 4, 5]

l4.extend(l3)
print(l4)  # [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
print("===========================")

# Example12: compare the lists
li4 = (10,20,30)
li5 = (10,20,30)
if li4==li5:
    print("lists are equal")
else:
    print("lists are not equal")
