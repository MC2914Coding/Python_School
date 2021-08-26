def multiply(x,y):
 
    # 0 case
    if(y == 0):
        return 0
 
    # Add x one by one and take 1 off y for every interval
    if(y > 0 ):
        return (x + multiply(x, y - 1))
 
    # The case where y is negative. add 1 to y for every intervall
    if(y < 0 ):
        return -multiply(x, -y)
     
# Driver code
print(multiply(5, -11))