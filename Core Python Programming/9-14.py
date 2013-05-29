# 9-14: calc.py

import sys

log_file = 'calc.txt'

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        res = 'divided by zero.'
    return res

def mod(a,b):
    try:
        res = a % b
    except ZeroDivisionError:
        res = 'divided by zero.'
    return res

def power(a,b):
    try:
        res = a ** b
    except ZeroDivisionError, err:  # such as 0**-1
        res = str(err)
    return res

# operators in dictionary 
oprs = {'+':add,
        '-':sub,
        '*':mul,
        '/':div,
        '%':mod,
        '**':power}

def deal_args(args):
    '''
        call individual calculations and log.
    '''
    
    nums = tuple(int(x) for x in (args[0], args[2]))    # generator to tuple
    opr = args[1]
    
    f = open(log_file,'a')  # append to the file
    # writelines() must use string
    f.writelines([str(nums[0]),' ', opr,' ', str(nums[1]),'\n'])
    
    if opr in oprs.keys():
        result = oprs[opr](*nums) # use variable-length arguments
        f.writelines([str(result), '\n'])

    f.close()

def dump_file():
    try:
        f = open(log_file,'r+') # open for writing
    except IOError:
        print 'Empty file.'
        return
    
    for line in f:
        print line,
    f.truncate(0)   # read all and empty file
    f.close()

def usage():
    print '''
Usage:
    num1 opr num2: deal the calculation and write to result file.
    print : output the result file and empty it.
    help : print this help.
'''
    
def main():
    args = sys.argv[1:]

    if len(args)<1 or len(args)>3:
        print 'Wrong arguments number.'
        usage()
        return
    
    if args[0]=='print':
        dump_file()
    elif args[0]=='help':
        usage()
    elif len(args)==3:
        deal_args(args)
    else:
        print 'Wrong arguments number.'
        usage()

def test():
    testcases = [
        'print',
        'help',
        '1+2',  # no space
        '1 + 2',
        '1 +2', # no space before '2'
        '1 - 2',
        '2 * 3',
        '2 / 3',
        '2 / 0', # divided by 0
        'print', # check result
        '5 / 2',
        '5 % 2',
        '5 % 0',    # divided by 0
        '5 % -1 ',
        '5 % -2',
        '2 ** 10',
        '2 ** -1',
        '0 ** 0',
        '0 ** -1',
        'print'
        ]

    for t in testcases:
        print 'test: ', t
        sys.argv[1:] = t.split()
        
        if t=='print':
            print '-'*20
            
        main()
        
        if t=='print':
            print '-'*20
    
if __name__=='__main__':
    # main()
    test()
