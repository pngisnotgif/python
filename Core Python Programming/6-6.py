# 6-6

def str_strip(s):
    print "'%s'==>"%(s),
    i = 0
    l = len(s)
    while i<l:
        if s[i]==' ':
            i += 1
        else:
            break

    if i>0:
        s = s[i:]
    
    l = len(s) - 1
    while l>=0:
        if s[l]==' ':
            l -= 1
        else:
            break
        
    if l>=0:
        s = s[:l+1]

    print "'%s'"%(s)


if __name__=='__main__':
    tests = ['', ' ', '  ', 'a', ' a', '  a', 'a ', 'a  ', ' a ','  a  ',
             ' a b a ']
    for i in tests:
        str_strip(i)
    
