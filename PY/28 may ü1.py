userfile = input("Name der Datei: ")

o = open(userfile, "x")

o = open(userfile, "w")
o.write("""
HERZLICH WILLKOMMEN! 
Eine Schule, zwei Abteilungen, drei Angebote. 
Wirtschaftsgymnasium 
Wirtschaftsmittelschule 
Informatikmittelschule 
""")

while True:
    a = input("text der neuen zeile: ")
    if a != 'q':
        o.write(a + "\n")
    else:
        o.close()
        break