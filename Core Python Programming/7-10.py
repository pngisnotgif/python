# 7-10

import string

def rot13(str_in, keep_case = True):
    srcstr = string.ascii_lowercase
    src = srcstr
        
    ret = ''
    for c in str_in:
        if keep_case:
            c_case = c.lower()  # use c_case(should be lower letter) to search
        else:
            c_case = c
       
        if c_case in src:
            i = src.index(c_case)
            if i<13:
                enc = src[i+13]
            else:
                enc = src[i-13]

            if c_case != c: # original letter is upper
                ret += enc.upper()
            else:
                ret += enc   
        else:
            ret += c

    return ret

if __name__=='__main__':

    test_cases = [
        'a',
        'm',
        'n',
        'z',
        'A',
        'M',
        'N',
        'Z',        
        'abcdefghijklmnopqrstuvwxyz',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '123~@#',
        'This is a short sentence.',
        'Guvf vf n fubeg fragrapr.'
        ]
    
    for str_in in test_cases:
        print "%s ==> %s"%(str_in, rot13(str_in))
