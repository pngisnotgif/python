# 8-7: perfect number

# QUESTION: how to import user functions? 
# from 8-5 import getFactors

# this function has been already realized in 8-5.py
def getFactors(n):
    factors = [1]

    for i in range(2,n):
        if n%i==0:
            factors.append(i)

    if n>1:
        factors.append(n)

    return factors

def isPerfect(n):
    factors = getFactors(n)
    factors.remove(n)   # in fact, we can also divide sum of factors by 2.
    
    if n==sum(factors):
        return True
    else:
        return False
    
if __name__=='__main__':

    # perfect_numbers = [i for i in range(1,100000) if isPerfect(i)]
    
    # This is not so good, because the list can only be printed out \
    # when all the proper numbers are estimated.
    
    for i in xrange(1,10000):
        if isPerfect(i):
            print "found perfect numbers: " , i
        
    
