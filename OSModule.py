#Program to show various Python OS Module 
import os

#Print Current Working Directory
cwd = os.getcwd()
print("Current working directory : ", cwd)

#Display list of files and directories
print(os.listdir())

#Check the OS module
print("The Operating system module is '% s'" % os.name)

#Remove a file Test.py
# os.remove(os.path.join(cwd,"Test.py"))

#Opening a file and read
try:

    path = os.path.join(cwd,"README.md")
    file = open(path, 'r')
    print(file.read())
    # file.write("Learning Python")
    # print(file.read())
    file.close()

    #Renaming a file
    path = os.path.join(cwd, "Pyton Handbook.pdf")
    file1 = "Python Handbook.pdf"
    os.rename(file1, "Python_Handbook.pdf")

except IOError:
    print("File % s not found"% "README.md")

