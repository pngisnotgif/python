# 11-12

# def timeit(func, times, *nkwargs, **kwargs):
# how to run many times? using times as a default parameter.
# and how to call timeit()? 
def timeit(func, *nkwargs, **kwargs):
    import time
    
    start_time = time.clock()
    try:
        # for i in range(times):
        #     retval = func( *nkwargs, **kwargs )
        retval = func( *nkwargs, **kwargs )
        
        end_time = time.clock()
        elapse_time = end_time - start_time
        result = (retval, elapse_time)
    except Exception, diag:
        result = (False, str(diag))

    return result

def test_time():
    funcs = (int, long, float)
    values = (1234, 12.34, '1234', '12.34')

    for eachfunc in funcs:
        print '-'*20
        for eachvalue in values:
            # result = timeit( eachfunc, eachvalue, times=10000 )
            result = timeit( eachfunc, eachvalue )
            
            if result[0] != False:
                print '%s(%s)=%s, Elapse time: %s secs.'\
                      %(eachfunc.__name__, repr(eachvalue), result[0], result[1])
                # note: eachfunc is a type<int> like variable.
                # Use __name__ to print its name.
                # use repr() to print the type of parameters.
            else:
                print '%s(%s) failed: %s.'%(eachfunc.__name__, repr(eachvalue), result[1])

    
if __name__=='__main__':
    test_time()
