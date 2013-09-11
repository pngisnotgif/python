# use lambda in iterator

def a():
    print 'func a'

def b():
    print 'func b'

def c():
    print 'func c'

def odd():
    func = []
    for f in 'abc':
        func.append((lambda f=f:f))
        # exec f + '()'
    return func

func_list = odd()

for func in func_list:
    func()  # how to call a(), b() or c()?
    if callable(func): pass
        # print type(func()),

