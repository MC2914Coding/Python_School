#Search for a File in a Directory
import os
user_file_conent = input("What's the Content of the file you're looking for? \n")


x = os.path.abspath(os.getcwd()) #get the current root
for root, dirs, files in os.walk(x): #loop thorugh the root, the directorys and the files
    for name in files: #loop trough all the files
      f = open(name, "r")
      file_contents = f.read()
      #print(file_contents)
      if(file_contents == user_file_conent):
      #print current path 
        print(name)
        


#if name.startswith(('''File''')): #check for the name