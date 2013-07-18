
import re

def match_phone(pattern):
    for t in testcase:
        m = re.match(pattern,t)
        print t, ':',
        if m:
            print 'PASS'
        else:
            print 'FAIL'

def test_ex15_28():
    r = r'(\d{3})?-?\d{3}-\d{4}'
    match_phone(r)

def test_ex15_29():
    r = r'\(?(\d{3})?[-)]?\d{3}-\d{4}'
    match_phone(r)
    
if __name__=='__main__' :
    testcase = ['800-555-1212',
                '555-1212',
                '(800)555-1212'
                ]
    test_ex15_28()
    print
    test_ex15_29()
