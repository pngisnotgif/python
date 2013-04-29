# 6-10

def capital_reverse(s):
    new_s = ''
    for i in s:
        if i.islower() :
            new_s += i.upper()
        elif i.isupper() :
            new_s += i.lower()
        else:
            new_s += i

    print s,'==>',new_s

def capital_reverse_v2(s):
    print s,'==>',s.swapcase()
    
if __name__=='__main__':
    testcases = ['Mr.Ed', 'mR.eD', 'abc', '', ' ', 'aBc', 'A', 'AB']
    for i in testcases:
        capital_reverse(i)
        capital_reverse_v2(i)
