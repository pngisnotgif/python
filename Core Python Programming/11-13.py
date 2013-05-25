# 11-13

# iterative
def iterative(n):
    res = 1
    for i in xrange(1,n+1):
        res *= i

    return res

def mult(x, y):
    return x*y

# using reduce and normal function
def reduce_mult(n):
    return reduce(mult, range(1,n+1))

# using reduce and lambda
def reduce_lambda(n):
    return reduce(lambda x,y:x*y, range(1,n+1))

# recursive
def recursive(n):
    if n==0 or n==1:
        return 1
    else:
        return n*recursive(n-1)
    
# Conclusion:
# iterative is fast. Using lambda or mult are similar.
# recursive is slowest and stack consuming
def test_factorial():
    n = 100
    funcs = [iterative, reduce_mult, reduce_lambda, recursive]

    try_times = 100000

    print 'Running %d times: '%(try_times)

    for f in funcs:
        result = timeit(try_times)(f,n)
        if result[0]!='Error:':
            print '%d! = %d'%(n, result[0]), \
                  '\n\tUsing %s: elapsed time: %.3f secs.'%(f.__name__, result[1])
        else:
            print 'Calling %s failed: %s'%(f.__name__, result[1])
        print

import time

# using timeit in 11-12.py
def timeit(times=1):

    def wrap( func, *nkwargs, **kwargs):
        start_time = time.time()
        try:
            for i in range(times):
                retval = func( *nkwargs, **kwargs )
            
            end_time = time.time()
            elapse_time = end_time - start_time

            result = (retval, elapse_time)
        except Exception, diag:
            result = ('Error:', str(diag))

        return result

    return wrap    
    
if __name__=='__main__':

    test_factorial()
