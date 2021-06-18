#Search for a File in a Directory
import os
user_file = input("What Files are you searching for? \n")
x = os.path.abspath(os.getcwd()) #print current path 
for root, dirs, files in os.walk(x):
    for name in files:
        if name.startswith((user_file)):
            # whatever #print current path 
            print(root, name)


