userinput = input("Wie heisst ihre datei? \n")

if(userinput == "myfile.txt"):
  f = open(userinput, "w")
  f.write("""
  WMS
  IMS
  """)

  f = open(userinput, "r")
  for x in f:
    print(x)

else:
  a = open(userinput, "x")