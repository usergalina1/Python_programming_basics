# create string variable

# Example1:  ways to creating string variables
s = 'welcome'
n = "welcome"
a = str('welcome')
b = str("welcome")

# creating empty strings variables
name = str()
name1 = ''
name2 = ""

# Example2:
# mutable- cannot change the value of the variable
# immutable- can change the value of the variable

# string is immutable
# if the value is changed after updating then it is immutable

str1 = "welcome"
print(id(str1))  # id of variable 2757577390704

str1 = str1 + "welcome"
print(id(str1))  # id of variable 2514112592880
print("====================")

# Example3: + and * with string
str = "welcome"
print(str + "programming")  # welcomeprogramming  (concatenation/joining)
print(str * 3)  # welcomewelcomewelcome
print("====================")

# Example4: Slicing operator []
str2 = "welcome"
print(str2[1:3])  # el
print(str2[:6])  # welcom  starting index is 0 by default
print(str2[2:])  # lcome
print(str2[1:-1])  # elcom  last 1 char is removed
print(str2[1:-2])  # elco   last 2 chars are removed
print("====================")

# Example5: ord()  and chr()
print(ord("A"))  # 65 (returns the ASCII code of the character)
print(chr(65))  # A  (returns character represented by a ASCII number)
print("====================")

# Example6: max()   min()   len()
print(max("abc"))  # c
print(min("abc"))  # a
print(len("abc"))  # 3
print("====================")

# Example7: in, not in operators - return true or false
z = "welcome"
print("come" in s)  # True
print("lome" in s)  # False
print("====================")

print("come" not in s)  # False
print("lome" not in s)  # True
print("====================")

# Example8: String comparison
print("tim" == "tie")  # False
print("free" != "freedom")  # True
print("arrow" > "aron")  # True
print("right" >= "left")  # True
print("teeth" < "tee")  # False
print("yellow" <= "fellow")  # False
print("abc" > "")  # True
print("====================")

# Example9: Testing strings True/False
c = "welcome to python"
print(c.isalnum())  # False      Checked if it's a number
print("Welcome".isalpha())  # True checked if it's alphabetical characters
print("2022".isdigit())  # True checked if it has digits
print("first Number".isidentifier())  # False      Checked if it contains key
print(c.islower())  # True checked if it has all lower case
print("WELCOME".isupper())  # True checked if it has all upper case
print(" ".isspace())  # True checked if it has a space
print("====================")

# Example10: Searching for substrings
d = "welcome to python"
print(d.endswith("thon"))  # True
print(d.startswith("good"))  # False
print(d.find("come"))  # 3 find the position (starts from 1)
print(d.find("become"))  # -1 not found
print(d.count("o"))  # 3 returns the number of occurrences of substring the string
print("====================")

# Example11: Converting String
q = "String in PYTHON"
q1 = q.capitalize()
print(q1)  # String in python  (Capitalize only the first letter of the string)

q2 = q.title()
print(q2)  # String In Python  (Each word start from capital letter)

q3 = q.lower()
print(q3)  # string in python

q5 = q.upper()
print(q5)  # STRING IN PYTHON

q5 = q.swapcase()
print(q5)  # sTRING IN python  (upper -> to lower, lower -> to upper)

q6 = q.replace("in", "on")
print(q6)  # Strong on PYTHON
print("====================")

# Example11: Reverse a string
  #Method1
x = "welcome"
rev_str = ""
for i in x:
    rev_str = i + rev_str
print("Reversed string is:", rev_str)  # emoclew

  # Method2 using slicing operator
x1 = "python"
rev_str1 = x1[::-1]  # x1[start:end:-1] or [0:7:-1]
print(rev_str1)  # nohtyp

