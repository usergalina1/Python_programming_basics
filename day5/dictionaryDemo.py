'''
A dictionary is a collection which is unordered, changeable(mutable) and indexed.
In Python dictionaries are written with curly brackets, and they have keys and values {}
'''

# Example1: creating dictionary
mydic = {101: "x", 102: "y", 103: "z"}
print(mydic) # {101: 'x', 102: 'y', 103: 'z'} it's not ordered, it can be not ordered
print("===================================")

#Example2: access items from dictionary
mydic ={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2021
}
print(mydic["brand"]) # Hyundai
print(mydic["model"]) # i10

#using get()
x=mydic.get("brand")
print(x)  # Hyundai
print("===================================")

#Example3: change values in dictinary
mydic1 ={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2020
}
print(mydic1) # {'brand': 'Hyundai', 'model': 'i10', 'year': 2020}
mydic1["year"]=2021
print(mydic1)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2021}
print("===================================")

#Example4: reading items from dictionary using loop
mydic2 ={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2020
}
for i in mydic2:
    print(i)  # captures only keys
'''
brand
model
year
'''
for i in  mydic2:
    print(mydic2[i]) # captures values
'''
Hyundai
i10
2020
'''
for i in mydic2.values():
    print(i)
'''
Hyundai
i10
2020
'''
for i in mydic2.items():
    print(i)
'''
('brand', 'Hyundai')
('model', 'i10')
('year', 2020)
'''
for x,y in mydic2.items():
    print(x,y) # prints keys along with the values
'''
brand Hyundai
model i10
year 2020
'''
print("===================================")

#Example5: check if key is exist in dictionary or not
mydic3 ={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2020
}
if "model" in mydic3:
    print("exist")
else:
    print("not exist")
# OR
print("model" in mydic3)  # True
print("===================================")

#Example6: find number of items in dictionary
mydic4 ={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2020
}
print(len(mydic4))  # 3
print("===================================")

#Example7: adding items to dictionary
mydic5 ={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2020
}
mydic5["color"]="red"
print(mydic5) # {'brand': 'Hyundai', 'model': 'i10', 'year': 2020, 'color': 'red'}
print("===================================")

#Example8: remove item from dictionary
mydic6 ={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2020
}
mydic5.pop("year")
print(mydic5)  # {'brand': 'Hyundai', 'model': 'i10', 'color': 'red'}

del mydic5["model"]
print(mydic5)  # {'brand': 'Hyundai', 'color': 'red'}

mydic6.clear()
print(mydic6)  # {} empty dictionary

del mydic6   # deleted dictionary completely
# print(mydic6)  # NameError: name 'mydic6' is not defined because we deleted the dictionary
print("===================================")

#Example9: copy dictionary
mydic6 ={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2020
}
# without using copy()
mydic7 = mydic6
print(mydic7)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2020}

# copy()
mydic8 = mydic6.copy()
print(mydic8)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2020}










