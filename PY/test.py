def multiply(x,y):
 
    # 0 multiplied with anything
    # gives 0
    if(y == 0):
        return 0
 
    # Add x one by one
    if(y > 0 ):
        return (x + multiply(x, y - 1))
 
    # The case where y is negative
    if(y < 0 ):
        return -multiply(x, -y)
     
# Driver code
print(multiply(5, -11))