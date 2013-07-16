#!/usr/bin/env python

# This script test regular expresions in chapter 15.
#
# It uses a self-defined test framework.


import re

# note: re.VERBOSE or re.X permits commentting after pattern
match = lambda r, t: re.match(r, t, re.VERBOSE) 
search = lambda r, t: re.search(r, t, re.VERBOSE)

def do_re_template(r, test_cases, func=match):
    if func is None or func not in (match,search):
        raise ValueError,'func should only within "match" and "search"'
    
    for t in test_cases:
        s = func(r,t)
        print t,
        if s:
            print ': OK!'
        else:
            print ': NOT match'
    
def test_ex15_1():
    r = '[bh].+t'
    test_cases = ['bat','bit','but','hat','hit','hut','haa','batch']
    do_re_template(r, test_cases, search)

def test_ex15_2():
    r = '\w+ \w+'
    test_cases = ['Jim Kerry','JimGreen', 'Tom Hanks Jr.']
    do_re_template(r, test_cases, match)

def test_ex15_3():
    r = '[a-zA-Z], \w+'
    test_cases = ['J, Kerry','J, Roberts','T. Hanks']
    do_re_template(r, test_cases, match)

def test_ex15_4():
    r = '([a-zA-Z_]+)(\w*)'
    t = ['abc', ' ', 'a123', '123', '_', '_12', 'A_', '__']
    do_re_template(r, t, match)

def test_ex15_5(): pass

def test_ex15_6():
    r = r'(w{3})\.(\w+)\.(com|edu|net|org|gov)'
    t = ['www.yahoo.com',
         'www.ucsc.edu',
         'http://www.yahoo.com',
         'g.cn',
         'google.com',
         'www.zhihu.net',
         'www.whitehouse.gov',
         'ww.123.org',
         'www.123.org',
        ]
    do_re_template(r, t, search)

def test_ex15_7():
    r = r'[-]?(\d+|0[xX][0-9a-fA-F]+)$'
    t = ['123',
         '-12',
         '0x2A',
         '0XDEAD111BEAF222c',
         '-027',
         '0101',
         '1e38',    # not supported, it is a float
         '0XX',
         'xa',
         'The digit'
        ]
    do_re_template(r, t, match)

def test_ex15_8():
    r = r'[-]?(\d+|0[xX][0-9a-fA-F]+)[lL]$'
    t = ['123',
         '123L',
         '0xdeadl',
         '-2342349238L'
        ]
    do_re_template(r, t, match)

def test_ex15_9():
    r = r'[-]?[0-9]+\.[0-9]*([eE]?[-]?\d+)*$'
    t = ['0.0',
         '-777.',
         '1.6',
         '-3.1415',
         '4.3e25',
         '1.000001',
         '-1.609E-19',
         '6.022e23',
         '-90.',
         '-10',
         '.',
         '.1',  # this reg-exp only support float with integral part
        ]
    do_re_template(r, t, match)

def test_ex15_10():
    '''
        complex number
    '''
    
    r = r'''            # pattern in nicer lines
            [-]?        # minus sign
            (           # real part
              \d*\.?\d+         # exponent part
              ([eE]?[+-]?\d+)?    # rank part
            )   
            [+-]        # sign of imaginary part
            (           # imaginary part
              \d*\.?\d+         # exponent
              ([eE]?[+-]?\d+)?  # rank
            )
            [jJ]$        # flag of imag. part
        '''
    
    # pattern in one line         
    # r =  r'[-]?(\d*\.?\d+([eE]?[+-]?\d+)?)[+-](\d*\.?\d+([eE]?[+-]?\d+)?)[jJ]'
    
    t = ['64.375+1j',
         '4.23-8.5j',
         '0.23-8.55j',
         '1.23e-045+6.7e+089j',
         '-1.23-865J',
         '0+1j',
         '-.0224+0j',
        ]
    do_re_template(r, t, match)

def test_ex15_11():
    r = r'[a-zA-Z]+\w*@(\w+\.)+(com|cn|gov|net|org)'
    t = ['abc@yahoo.com',
         'a12_3@knd.cn',
         'test@abc.gmail.com',
         't1@.com',
         '1a@g.cn',
         't@s.net'
        ]
    do_re_template(r, t, match)

def test_ex15_12():
    # url

    r = r'''
            ((http|https|ftp|telnet|file)://)?  # protocol
            (w{3}\.)?                           # www
            (\w+\.)*                            # domain name
            (com|cn|org|gov|net)                # DOES NOT parse ip addr.
            #(/\w+)*$                           # path and file
        '''
    t = ['g.cn',
         'www.abc.com',
         'http://www.knd.com.cn/aboutus',
         'file://test.server.com/path/filename',
         'ftp://192.168.0.1/file/file1'
        ]
    do_re_template(r, t, match)
    
def count_test_defs():
    '''
        count test function in this file, starting with 'test_'
    '''
    
    import sys
    import os.path
    filename = os.path.basename(sys.argv[0])    # get this script's filename

    r = '^def test_(\w+)'    # all test functions start with 'test' without comment sign
    count = 0
    with open(filename) as f:
        for line in f.readlines():
            m = re.match(r, line)
            if m:
                count += 1

    return count

def get_declaration_testsuite():
    '''
        declare all testcases in testsuite, return a python expresion to exec
    '''
    
    def_prefix = 'test_ex15_'
    def_lists = '['
    func_nums = count_test_defs()
    
    for i in range(1, func_nums+1):
        def_lists += def_prefix + str(i) + ', '
        
    def_lists += ']'
    cmd = 'test_suite = ' + def_lists
    return cmd

def run_all_tests():
    for test in test_suite:
        print '[', test.__name__, '] :'
        test()
        print

def run_last_tests():
    test_suite[len(test_suite)-1]()
    
if __name__=='__main__':
    
    declare_testsuite = get_declaration_testsuite()
    exec(declare_testsuite) # declare all the testcases
    
    run_last_tests()
    # run_all_tests()
