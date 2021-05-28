y = 11
c = " "
x = 1
b = "*"

while(y > 0):
    print((c*y)+("*"*x)+("*"+b*x))      #print((leerzeichen von 10 - 1)+(stern von 1 - 10)+(* + * von 1 - 10))
    x = x + 1                           #/\
    y = y - 1

while(y < 12):
    print((c*y)+("*"*x)+("*"+b*x))      #print((leerzeichen von 1 - 10)+(stern von 10 - 1)+(* + * von 10 - 1))
    x = x - 1                           #\/
    y = y + 1
