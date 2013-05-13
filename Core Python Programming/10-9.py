# 10-9

import math
import cmath

def safe_sqrt(x):
    
    try:
        res = math.sqrt(x)
    except ValueError:
        try:
            print '\tin VauleError solver'
            res = cmath.sqrt(x)
        except:
            pass
    except TypeError:
        if type(x)==type(complex(0,1)): # x is a complex 
            res = cmath.sqrt(x)
        else:
            print 'TypeError: x should be a float or complex number.'
            res = None
    finally:
        return res

if __name__=='__main__':
    tests = [4,1,0,-1,1+2j,'a',[2]]
    for i in tests:
        print "sqrt(%s)=%s"%(i,safe_sqrt(i))
    
