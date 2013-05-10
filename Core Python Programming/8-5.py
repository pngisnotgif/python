# 8-5
# get factors

def getFactors(n):
    factors = [1]

    for i in range(2,n):
        if n%i==0:
            factors.append(i)

    if n>1:
        factors.append(n)

    return factors
    

if __name__=='__main__':
    for i in range(1,100):
        print "factors of %d: "%i, getFactors(i)
