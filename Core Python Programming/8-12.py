# 8-12

import string

def print_head(has_ascii = True):
    slash_num = 30
    table_head = "DEC\tBIN\tOCT\tHEX"
    
    if has_ascii:
        table_head += "\tASCII"
        slash_num += 10      

    print table_head
    print '-'*slash_num

def print_rows(n, has_ascii = True):
    # bin, oct and hex, generates string
    # print "%3d   %7s\t%s\t%s"%(n, bin(n)[2:], oct(n)[1:], hex(n)[2:]),

    print "%3d\t%6s\t%3o\t%3x"%(n,bin(n)[2:],n,n),
    if has_ascii:
        c = chr(n)
        if c in string.printable:
            print "\t%s"%c
        else:
            print
    else:
        print

def print_table(start, end):
    printable_strs = string.printable
    
    found_printable = False
    for c in range(start, end+1):
        if chr(c) in printable_strs:
            found_printable = True

    print_head( found_printable )
    for i in range(start, end+1):
        print_rows(i, found_printable )

    print
    
if __name__=='__main__':
    tests = [
        [1,8],
        [9,18],
        [19,31],
        [26,41]
        ]

    for i in tests:
        print_table(i[0], i[1])
