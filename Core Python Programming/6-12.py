# 6-12

def findchr(string, char):
    
    if len(char)>1:
        print "Warning: Wrong length of target char '%s'."%(char)
        return -1
    
    if char in string:
        i=0
        for c in string:
            if c==char:
                return i
            else:
                i += 1

    return -1

def rfindchr(string, char):

    if len(char)>1:
        print "Warning: Wrong length of target char '%s'."%(char)
        return -1

    for i in range(len(string)-1,-1,-1):    # list generated using range is before used with for
        if string[i]==char:
            return i
    else:
        return -1

def subchr(string, origchar, newchar):
    '''
        This function can only replace the first target.

        While, it can also replace all the origchar(s) using 'for'.
        I realize it calliing 'findchr' above.
    '''
    
    index = findchr(string, origchar)
    if index > -1:
        newstring = string[:index] + newchar + string[index+1:]
        print "'%s'('%s'-->'%s'):'%s'"%(string, origchar, newchar, newstring)
    else:
        print "No target found."

if __name__ == '__main__':
    testcases = [ 
                  ['',''],
                  [' ', ''],
                  ['str','s'],
                  ['str','t'],
                  ['str','r'],
                  ['str','b'],
                  ['str','ab'],
                  ['str','tr'],
                  ['sts','s'],
                  ['ttt','t'],
        ]
    for s,c in testcases:
        print "'%s' in '%s': %d "%(c,s,findchr(s,c))
        print "'%s' in '%s' from right: %d "%(c,s,rfindchr(s,c))
        subchr(s,c,'a')
