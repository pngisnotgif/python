# 8-9: fibonacci
# 11-14: recursive method, and using timeit

def getNthFib(n):
    a = 1
    b = 1
    if (n==1):
        return a
    elif (n==2):
        return b

    i = 2
    while(i<n):
        a, b = b, a+b
        i += 1
    return b

# using recursive method in 11-14.py
# paramater n more than 40 may not work
def getNthFib_recursive(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return getNthFib_recursive(n-2) + getNthFib_recursive(n-1)

import time
def timeit(times = 1):
    def wrap(func, *args, **kwargs):
        start_time = time.time()

        try:
            for i in range(times):
                res = func(*args, **kwargs)
        except Exception, diags:
            result = ['Error', str(diags)]
            return result
        except KeyboardInterrupt:
            end_time = time.time()
            elapsed_time = end_time - start_time
            res = 'Break'   # calculate elapsed time, also
            result = [res, elapsed_time ]
            
        end_time = time.time()
        elapsed_time = end_time - start_time
        result = [res, elapsed_time]
        return result
        
    return wrap

def test_fibonacci(n):
    funcs = [getNthFib,getNthFib_recursive ]
    res_tuple = '(f.__name__, result[1])'
    for f in funcs:
        for i in range(1,n):
            result = timeit()(f,i)
            if result[0]=='Error':
                print "running function %s failed: %s"%eval(res_tuple)
                break
            elif result[0]=='Break':
                print "function %s breaks at %.3f secs."%eval(res_tuple)
                break
        else:
            print"elapsed time of running function %s: %.3f secs."\
                          %eval(res_tuple)
    
if __name__=='__main__':
    test_fibonacci(35)
