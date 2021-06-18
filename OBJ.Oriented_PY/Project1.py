#Search for a File in a Directory
import os
user_file = input("What Files are you searching for? \n")
x = os.path.abspath(os.getcwd()) #get the current root
for root, dirs, files in os.walk(x): #loop thorugh the root, the directorys and the files
    for name in files: #loop trough all the files
        if name.startswith((user_file)): #check for the name
            #print current path 
            print(root, name)


