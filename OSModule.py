# <<<<<<< HEAD
#Program to show various Python OS Module 
# =======
#Program to show various Python OS Module for accessing OS commands
#import os package 

# >>>>>>> 1ef2ab2 (OSModule.py modified comments)
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
    path = os.path.join(cwd, "Pyton_Handbook.pdf")
    # file1 = "Python Handbook.pdf"
    # os.rename(file1, "Python_Handbook.pdf")

    #Printing file size
    size = os.path.getsize("Python_Handbook.pdf")
    print(size)

except IOError:
    print("File % s not found"% "README.md")

