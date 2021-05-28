y = 11
c = " "
x = 1
b = "*"

while(y > 0):
  print((c*y)+"*"+(c*x) + (c*x)+"*"+(c*y))
  x = x + 1                           
  y = y - 1

while(y < 12):
  print((c*y)+"*"+(c*x) + (c*x)+"*"+(c*y))
  x = x - 1                           
  y = y + 1
