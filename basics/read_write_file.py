# Open the file read only 
file = open("basics/file.txt", "r")
print(file.readline())
#print(file.readlines())

#By default the read() method returns the whole text, 
# but you can also specify how many characters you want to return:
print(file.read(20))

# By looping through the lines of the file, 
# you can read the whole file, line by line:
for x in file:
    print(x)

file.close()


"""
To write to an existing file, you must add a parameter to the open() function:
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"""
file = open("basics/file.txt","a")
file.write("\n This is the best song ever!")
file.close()

file = open("basics/file.txt","r")
print(file.read(-30))
file.close()

file = open("basics/file.txt", "w")
file.write("Oops.. I did it again!")
file.close()

file = open("basics/file.txt", "r")
print(file.read())
file.close()
