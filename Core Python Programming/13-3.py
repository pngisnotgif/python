# 13-3
    
class MoneyFmt(object):
    '''
        A class deals with money format.
    '''
    
    def __init__(self, value):
        if isinstance(value, (float,int)):  # should be float or integer
            self.__data = value
        else:
            msg = "Type of '%s' error, should be float."%(value)
            raise TypeError, msg

    def dollarize(self, grouping = True):
        if self.__data>=0:
            s = '${:,.2f}'.format(self.__data)  # new style of string formatter
        else:
            s = '-${:,.2f}'.format(abs(self.__data))
        
        #s = "$%.2f"%(self.__data)
        #if grouping:
        #    s = group(s)
        
        return s

    __str__ = dollarize

    def __repr__(self):
        return repr(self.__data)

    def update(self, newvalue):
        if isinstance(newvalue, (float, int)):
            self.__data = newvalue
        else:
            msg = 'Wrong type of newvalue'
            raise TypeError, msg

    def __nonzero__(self):
        return self.__data!=0

def test():
    a = MoneyFmt(123456.789)
    print a
    
    b = MoneyFmt(-123456.789)
    print b
    
    a.update(34567890.456)
    print a
    
    print bool(a)
    
    b.update(0.5)
    print bool(b)


if __name__=='__main__':
    test()
