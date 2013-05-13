# 10-7

def test_try_1():
    print 'try-except-else:'
    try:
        print 'statement A executed.'
        # raise IOError # Exception
    except IOError :
        print 'except statement executed.'
    else:
        print 'statement B executed.'
        raise IOError

def test_try_2():
    print 'try-except: '
    try:
        print 'statement A executed.'
        # raise IOError
        print 'statement B executed.'
        raise IOError
    except IOError :
        print 'except statement executed.'

if __name__=='__main__':
    test_try_1()    # comment this statement to run test_try_2()
    print
    test_try_2()
