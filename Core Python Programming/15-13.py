# 15-13

import re

def get_type_name(s):
    pattern = r"<type '(\w+)'>$"
    m = re.match(pattern, s)
    if m:
        return m.group(1)
    else:
        return None

def test():
    class A(object): pass
    a = A()
    test_values = [1, '1', 1.2, dir, A, a, type]
    testcases = [ str(type(x)) for x in test_values ]   # generate type string
    for s in testcases:
        res = get_type_name(s)
        if res:
            print 'type =', res
        else:
            print 'not a type'

if __name__=='__main__':
    test()
            
