# 11-12

import time

def timeit(times=1):

    def wrap( func ):
        def _wrap(*nkwargs, **kwargs):
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
        return _wrap
    return wrap

times = 20000

# use decorator
@timeit(times)
def test(func, value):
    return func(value)
    
def test_time():
    funcs = (int, long, float)
    values = (1234, 12.34, '1234', '12.34')

    for eachfunc in funcs:
        print '-'*20
        for eachvalue in values:
            result = test( eachfunc, eachvalue )   # notice the form of parameters.          
            
            if result[0] != 'Error:':
                print '%s(%s)=%s, Elapse time: %.4f secs.'\
                      %(eachfunc.__name__, repr(eachvalue), result[0], result[1])
                # note: eachfunc is a type<int> like variable.
                # Use __name__ to print its name.
                # use repr() to print the type of parameters.
            else:
                print '%s(%s) failed: %s.'%(eachfunc.__name__, repr(eachvalue), result[1])

    
if __name__=='__main__':
    test_time()
