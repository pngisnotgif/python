# 11-6 printf
# variable length arguments.

def printf(fmt, *args):
    if fmt != None:
        try:
            print fmt%(args)
        except TypeError:
            print 'The numbers of arguments may be wrong:'
            print "\tfmt: '%s', but arguments: %s"%(fmt, str(args))
    else:
        print

def test_printf():
    tests = [ ['hello, world!'],
              ['a=%d',1],
              [],
              ['a=%d, b=%d', 1, 2],
              ['a=%d, b=%f', 1,2.0],
              ['a=%d, b=%f, c=%s', 1, 1.23, 'hello'],
              ['a=%%, b=%d',1],
              ['a=%%, b=%d',1,2],   # more arguments 
              ['a=%%, b=%d']        # less arguments

        ]

    for i in tests:   
        if len(i)==1:
            printf(i[0])
        elif len(i)==0:
            printf(None)
        else:
            printf(i[0],*i[1:]) # an asterisk: '&' should be used before tuple
        

if __name__=='__main__':
    test_printf()

    # This is direcly calling printf
    printf('%d+%d=%d',1,2,1+2)
