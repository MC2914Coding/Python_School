def kgV(m,n):
    """ calculate the least common multiple """
    if m == 0 or n == 0:
        print("kgV = 0")
    else:
        if m > n:
            m,n = n,m
        mCounter = m;
        while mCounter <= m*n:
            if mCounter % n == 0:
                print("kgV = ",mCounter)
                break
            mCounter += m
    return m
 
def main():
    print(kgV(0,6))