# 7-9
# character translation, like tr() in Unix

# v1.2 - support deleting chars problem
# v1.1 - support case ignoring
# v1.0 - basic function


def tr(srcstr, dststr, string, ignore_case = False):
    if len(srcstr)!=len(dststr):
        print 'Wrong length of srcstr and dststr, should be equal: (%s and %s)'\
              %(srcstr, dststr)
        ret = '(ERROR)'
        return ret

    if ignore_case:
        src = srcstr.lower()
        des = dststr.lower()
        str_in = string.lower()
    else:
        src = srcstr
        des = dststr
        str_in = string
        
    ret = ''
    for c in str_in:
        if c in src:
            ret += des[src.index(c)]
        else:
            ret += c

    return ret

# support deleting chars in condition len(s)>=len(d).
def tr_v2(srcstr, dststr, string, ignore_case = False):
    if len(srcstr) < len(dststr):
        print 'Wrong length of srcstr and dststr, should be equal or more: (%s and %s)'\
              %(srcstr, dststr)
        ret = '(ERROR)'
        return ret

    if ignore_case:
        src = srcstr.lower()
        des = dststr.lower()
        str_in = string.lower()
    else:
        src = srcstr
        des = dststr
        str_in = string
        
    ret = ''
    for c in str_in:
        if c in src:
            i = src.index(c)
            if i > len(des)-1:
                continue    
            else:
                ret += des[i]
        else:
            ret += c

    return ret
    
if __name__=='__main__':

    test_cases = [
        ['abc', 'mno', 'abcdef'],
        ['a','c','abcdef'],
        ['aac','mno','abcdef'], # same char in srcstr
        ['abc','a','abcdef'],   # wrong length of parameters
        ]

    test_cases_ignore = [
        ['aBc', 'Def', 'abcdef'],
        ['aA', 'BC', 'abcdef'],
        ['aA', 'bC', 'aAbBcC'],
        ['A','b','abc'],
        ['a','B','Abc'],
        ]

    test_cases_v2 = [
        ['abcdef','mno','abcdefghi'],
        ]

    # how to deal with varible arguments calling ?
    for s,d,string in test_cases:
        print "given (%s==>%s), %s ==> %s"%(s,d,string,tr(s,d,string))

    for s,d,string in test_cases_ignore:
        print "given (%s==>%s), %s ==> %s"%(s,d,string,tr(s,d,string,True))

    # test v2:
    # TODO: how to deal with function pointer?
    # i.e. call 'tr_v2' or 'tr' according to function parameter
    print 'v2:'
    for s,d,string in test_cases:
        print "given (%s==>%s), %s ==> %s"%(s,d,string,tr_v2(s,d,string))

    for s,d,string in test_cases_ignore:
        print "given (%s==>%s), %s ==> %s"%(s,d,string,tr_v2(s,d,string,True))

    for s,d,string in test_cases_v2:
        print "given (%s==>%s), %s ==> %s"%(s,d,string,tr_v2(s,d,string))
