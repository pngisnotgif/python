# 8-6

factorsToTry = [2]
def isPrime(n):
    if n<=1:
        return False

    if n==2:
        return True

    for i in factorsToTry:
        if n % i == 0:
            return False
    else:
        factorsToTry.append(n) 
        return True

def resolvePrimeNumber(n):
    prime_factors = []
    if n<2:
        return prime_factors

    if isPrime(n):  # calling isPrime() once can generate prime list less than it.
        prime_factors.append(n)
        return prime_factors
    else:
        finish = False
        i = 0
        divided = n
        while not finish:
            p = factorsToTry[i] # using prime list made before
            if divided % p == 0:
                prime_factors.append(p)
                divided = divided / p                
            else:
                i += 1  # when not divided exactly, try next prime

            if divided==1:
                finish = True

    return prime_factors

if __name__=='__main__':
    for i in range(1,100):
        print "Prime factors of %d: "%i, resolvePrimeNumber(i)
        

    
        
