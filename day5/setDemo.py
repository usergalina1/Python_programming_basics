# set : A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets {}
# set is mutable 

# Example1: creating set
myset = {"apple", "banana", "cherry"}
print(myset)  # {'apple', 'cherry', 'banana'}
print("=======================================")

#Example2: Accessing items from set
myset1 = {"apple", "banana", "cherry"}
for i in myset:
    print(i)
'''
apple
cherry
banana
'''
print("=======================================")

#Example3: value exist in set or not
myset2 = {"apple", "banana", "cherry"}
print("banana" in myset)  # True
print("banana2" in myset) # False
print("=======================================")

#Example4: adding items to set
# add() - add single item        update() -  add multiple items
myset3 = {"apple", "banana", "cherry"}
myset3.add("orange")
print(myset3)  # {'orange', 'apple', 'cherry', 'banana'}
myset3.update(["mango", "kiwi", "grapes", "cherry"])
print(myset3) # {'mango', 'kiwi', 'grapes', 'cherry', 'apple', 'orange', 'banana'}
print("=======================================")

#Example5: find number of items in a set len()
myset4 = {"apple", "banana", "cherry"}
print(len(myset4)) # 3
print("=======================================")

#Example6: remove item from set  remove() discard()
myset5 = {"apple", "banana", "cherry"}
myset5.remove("banana")
print(myset5)  # {'apple', 'cherry'}
# myset5.remove("xyz") # KeyError: 'xyz'

myset5.discard("cherry")
print(myset5) # {'apple'}
myset5.discard("xyz") # will not throw any error
print("=======================================")

#Example7: clear all items from set
myset6 = {"apple", "banana", "cherry"}
myset6.clear()
print(myset6) # set()

del myset6
# print(myset6) # NameError: name 'myset6' is not defined.
print("=======================================")

#Example8: joining 2 sets  union()   update()
set = {"apple", "banana", "cherry"}
set1 = {1, 2, 3, 4}
set3 = set.union(set1)
print(set3) # {1, 'cherry', 2, 3, 4, 'banana', 'apple'}

set2 = {"apple", "banana", "cherry"}
set4 = {1, 2, 3,10}
set2.update(set4)
print(set2)  # {1, 2, 3, 'apple', 'cherry', 10, 'banana'}









