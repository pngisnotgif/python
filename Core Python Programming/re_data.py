#!/usr/bin/env python

# This script test regular expresions in chapter 15, from 15-17 to 15~29.
#
# It uses a self-defined test framework.

import re

# note: re.VERBOSE or re.X permits commentting after pattern
match = lambda r, t: re.match(r, t, re.VERBOSE) 
search = lambda r, t: re.search(r, t, re.VERBOSE)

def do_re_template(pattern, string, func=match):
    if func is None or func not in (match,search):
        raise ValueError,'func should only within "match" and "search"'
    
    for t in string:
        s = func(pattern, string)
        if s:
            return s.group()
        else:
            return None
    
def test_ex15_17():
    '''
        count weedkay's frequency
    '''
    
    weekday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    r = '|'.join(weekday)

    # initilize every day's count
    count_weekday = dict( zip(weekday, (0 for i in range(len(weekday))) ) )

    # do regular match, and count
    for line in f.readlines():
        day = do_re_template(r, line, match)
        if day in weekday:
            count_weekday[day] += 1

    for day in count_weekday:
        print day, ':', count_weekday[day]
    print

def match_line(line, item):
    '''
        extract assigned item from every line of redata.txt
    '''
    
    r = r'(.+)::(.+)::(.+)'
    m = re.match(r, line)
    
    timestamp = m.group(1)
    email = m.group(2)
    ints = m.group(3)

    return m.group(item)

def test_ex15_18():
    '''
        verify timestamp
    '''
    
    from time import ctime

    longint_r = r'(\d+)-.+-.+'
    isTestPassed = True
    for line in f.readlines():
        ints = match_line(line, 3)
        time_int = re.match(longint_r, ints)
        if time_int:
            t = ctime( float(time_int.group(1)) )
            t_from_file = match_line(line, 1)
            # print t,t_from_file
            if t_from_file:
                if t == t_from_file:    # TODO: not works in mac: day without leading 0 pads
                    # print 'PASS!'     # because redata.txt is generated in windows
                    pass
                else:
                    isTestPassed = False    # ???? How to break to outmost here? 
            else:
                # print 'Timestamp NOT found!'
                isTestPassed = False
        else:
            # print 'time_int NOT found!'
            isTestPassed = False

    if isTestPassed:
        print 'PASS!'
    else:
        print 'FAIL!'

def test_ex15_19():
    '''
        print timestamp
    '''
    for line in f.readlines():
        print match_line(line, 1)

def test_ex15_20():
    '''
        print email address
    '''
    for line in f.readlines():
        print match_line(line, 2)

def test_ex15_21():
    r = r'\w{3} (\w{3}) .+'
    for line in f.readlines():
        timestamp = match_line(line, 1)
        try:
            month = re.match(r, timestamp).group(1)
            print month
        except AttributeError:
            print 'month not found.'

def test_ex15_22():
    r = r'.+(\d{4})'
    for line in f.readlines():
        timestamp = match_line(line, 1)
        try:
            year = re.match(r, timestamp).group(1)
            print year
        except AttributeError:
            print 'year not found.'            

def test_ex15_23():
    r = r'.+(\d{2}):(\d{2}):(\d{2})'
    for line in f.readlines():
        timestamp = match_line(line, 1)
        try:
            t = re.match(r, timestamp).group(1,2,3)
            print '{}:{}:{}'.format(t[0], t[1], t[2])
        except AttributeError:
            print 'time not found.'

def test_ex15_24():
    r = '(.+)@(.+)'
    for line in f.readlines():
        email = match_line(line, 2)
        try:
            login, domain = re.match(r,email).group(1, 2)
            print 'login: %s'%(login), '\t domain: %s'%(domain)
        except AttributeError:
            print 'login or domain not found.'

def test_ex15_25():
    r = '(.+)@(.+)\.(.+)'
    for line in f.readlines():
        email = match_line(line, 2)
        try:
            login, main_domain, top_domain = re.match(r,email).group(1, 2, 3)
            print 'login: %s'%(login), '\t m-domain: %s'%(main_domain),\
            '\t top-domain: %s'%(top_domain)
        except AttributeError:
            print 'login or domain not found.'    

def test_ex15_26():
    r = '\w+@\w+\.\w+'  # the string that matches in the string
    myemail = 'pngisnotgif@qq.com'
    newfile = open('redata_new.txt','w')
    for line in f.readlines():
        newline = re.sub(r, myemail, line)
        if newline:
            # print newline,
            newfile.write(newline)
    newfile.close()
            
def test_ex15_27():
    r = r'\w{3}\s(\w{3})\s(\d{2}).+(\d{4})'
    for line in f.readlines():
        timestamp = match_line(line, 1)
        try:
            month, day, year = re.match(r, timestamp).group(1, 2, 3)
            print '{} {}, {}'.format(month, day, year)
        except AttributeError:
            print 'timestamp not found.' 
    
def get_test_defs():
    '''
        get test function in this file, starting with 'test_'
    '''
    
    import sys
    import os.path
    filename = os.path.basename(sys.argv[0])    # get this script's filename

    r = r'^def (test_\w+)(\(.*\))'    # all test functions start with 'test' without comment sign
    with open(filename) as f:
        for line in f.readlines():
            m = re.match(r, line)
            if m:
                yield m.group(1)

def get_declaration_testsuite():
    '''
        declare all testcases in testsuite, return a python expresion to exec
    '''
    
    def_lists = '['
    gen_testcases = get_test_defs()
        
    for func_name in gen_testcases:
        def_lists += func_name + ', '
        
    def_lists += ']'
    cmd = 'test_suite = ' + def_lists
    return cmd

def run_all_tests():
    for test in test_suite:
        f.seek(0)
        print '[', test.__name__, '] :'
        test()
        print

def run_last_tests():
    test_suite[len(test_suite)-1]()
    
if __name__=='__main__':
    
    declare_testsuite = get_declaration_testsuite()
    exec(declare_testsuite) # declare all the testcases

    filename = 'redata.txt'
    with open(filename) as f:
        run_last_tests()
        # run_all_tests()
        # test_ex15_18()
