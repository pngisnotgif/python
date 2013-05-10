# 8-4

# isPrime()

from math import sqrt

factorsToTry = [2]
def isPrime(n):
    if n<=1:
        return False

    if n==2:
        return True

    # method 1:
    # maxFactorToTry = int(sqrt(n))   # O( n*sqrt(n) )

    # method 2:
    # maxFactorToTry = n-1          # O(n^2)
  
    # factorsToTry = [2]
    # if n > 2*2:
    #    factorsToTry.extend(x for x in xrange(3,maxFactorToTry+1,2))

    # method 3:
    # we can also save former results to improve efficiency

    for i in factorsToTry:
        if n % i == 0:
            return False
    else:
        factorsToTry.append(n) # method 3 added.
        return True

def findPrime(m):
    return [i for i in xrange(m) if isPrime(i)]

if __name__=='__main__':

    MAX_PRIME_RANGE = 100

    
    from timeit import Timer

    t1 = Timer("findPrime(10000)","from __main__ import findPrime")
    print "%.3f sec."%t1.timeit(100)
    

    '''
     # output primes within MAX_PRIME_RANGE
    primes = findPrime(MAX_PRIME_RANGE)
    total = len( primes )

    print primes
    print 'Total=',total
    '''
    
    

    
