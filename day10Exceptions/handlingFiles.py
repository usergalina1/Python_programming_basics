#Example 1 writing data into text file
file = open("/Users/gd/Desktop/DemoFiles/myFile.txt", 'w')
file.write("This is my 1first statement\n")
file.write("This is my 2second statement\n")
file.write("This is my 3third statement\n")
file.write("This is my 4forth statement")
file.close()
print("program completed")

# Example 2 reading data from text file
file = open("/Users/gd/Desktop/DemoFiles/myFile.txt", 'r')
# print(file.read())  # will print all lines from the file
print(file.readline()) # will print only the first line
file.close()

# Example 3 append data into text file
file = open("/Users/gd/Desktop/DemoFiles/myFile.txt", 'a')
file.write("\n This is my first or second statement\n")
file.write("This is my third or forth statement\n")
file.close()