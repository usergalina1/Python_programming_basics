num1=input("Enter first number:")
num2=input("Enter second number:")

print(type(num1)) #str
print(type(num2)) #str

print(num1+num2) #100200

# Approach 1
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

print(type(num1)) #int
print(type(num2)) #int

print(num1+num2) #300

# Approach 2
num1=input("Enter first number:")
num2=input("Enter second number:")

print(type(num1)) #str
print(type(num2)) #str

print(int(num1)+int(num2))

#Example (float)
num1=input("Enter first number:") #10.5
num2=input("Enter second number:") #12.8

print(type(num1)) #str
print(type(num2)) #str

print(float(num1)+float(num2)) #23.3



