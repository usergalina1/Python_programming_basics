'''
A Tuple is a collection which is ordered and unchangeable.
In Python it is written with round brackets. ()
Tuple is Immutable

it is impossible to
-modify existing value
- append a new value
- insert a new value
- remove a value
'''

# Example1: creating tuple
mytuple = ("apple", "banana", " cherry")
print(mytuple)  #('apple', 'banana', ' cherry')
mytuple2=()
print(mytuple2) # () empty tuple
print("===========================")

# Example2: access tuple items
mytuple1 = ("apple", "banana", " cherry")
print(mytuple1[1]) #  banana
print(mytuple1[-1]) # cherry
print("===========================")

# Example3: range of indexes
mytuple2 = ("apple", "banana", " cherry", "orange", "kiwi",  "melon", "mango")
print(mytuple2[2:5])  # (' cherry', 'orange', 'kiwi')
print(mytuple2[-4:-1])  # ('orange', 'kiwi', 'melon')
print("===========================")

# Example4: Changing tuple values
# By default tuple does not allow you to change values bcoz it's immutable.
# but there is work around
# tuple--> list(modify)--> tuple
mytuple3 = ("apple", 100, 15.6)
myList = list(mytuple3)
myList[0] = "orange"
mytuple3 = tuple(myList)
print(mytuple3)  # ('orange', 100, 15.6)
print("===========================")

# Example5: Reading tuple items using loop
mytuple4 = ("apple", 100, 15.6)
for i in mytuple4:
    print(i)
'''
apple
100
15.6
'''
print("===========================")

# Example6: Check if Item exists (searching of item in tuple)
mytuple4 = ("apple", 100, 15.6)
if "apple" in mytuple4:
    print("apple exists")
else:
    print("apple is not exists")
'''
apple exists
'''
print("===========================")

# Example7: Tuple Length - counting items in a tuple
mytuple5 = ("apple", 100, 15.6)
print(len(mytuple5)) # 3
print("===========================")

# Example8: Add items to the tuple -tuple does not allow you to add values bcoz it's immutable.
# work around
mytuple6 = ("apple", 100, 15.6)
list1 = list(mytuple6)
list1[1] = "orange"
mytuple6 = tuple(list1)
print(mytuple6) # ('apple', 'orange', 15.6)
print("===========================")

# Example9: copy tuple
mytuple7 = ("apple", 100, 15.6)
myNewTuple = mytuple7
print(myNewTuple) # ('apple', 100, 15.6)
print(mytuple7) # ('apple', 100, 15.6)
print("===========================")

# Example10: Remove items from tuple - not possible directly
mytuple8 = ("apple", 100, 15.6)
# mytuple8.remove("apple")  #invalid
del mytuple8
#print(mytuple8)    #invalid  NameError: name 'mytuple8' is not defined.
print("===========================")

# Example11: combine/join tuple
tuple1 = (10,20,30)
tuple2 = ("a",20,"b")
tuple3 = tuple1 + tuple2
print(tuple3)  # (10, 20, 30, 'a', 20, 'b')
print("===========================")

# Example12: compare the tuples
tuple4 = (10,20,30)
tuple5 = ("a",20,"b")
if tuple4==tuple5:
    print("tuples are equal")
else:
    print("tuples are not equal")




