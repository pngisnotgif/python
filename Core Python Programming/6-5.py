# 6-5

def test_palindrome(s, special):

    special_str = r'0abtnvfre"\''    # string that include \0, \a, ... 
    
    half_len_s = len(s) / 2
    i = 0
    while(i<half_len_s):
        if not special:
            if s[i]!=s[-i-1]:
                print "'%s' is not a palindrome string."%(s)
                break;
        else:
            if ((s[i]=='\\') and (s[i+1] in special_str)):
                if (not ((s[i+1]==s[-i-1]) and (s[-i-2]=='\\') )):
                    print "'%s' is not a palindrome string."%(s)
                    break;
                else:
                    i += 1
            else:
                if s[i]!=s[-i-1]:
                    print "'%s' is not a palindrome string."%(s)
                    break;
        i += 1
    else:
        print "Yes! '%s' is a palindrome string."%(s)

def make_palindrome(s):
    import copy
    new_s = copy.copy(s)
    for i in range(len(s), 0, -1):
        new_s += s[i-1]
    print "'%s' ==> '%s'"%(s,new_s)
    

def test_simple_palindrome():
    simple_test = ['', ' ', 'a', 'ab', 'abc', 'aa', 'aba', 'abba',
                   ]
    for s in simple_test:
        test_palindrome(s,False)
        

def test_extended_palindrome():
    extended_test = [r'\0', r'\00', r'\n', r'\t', r'\"', r'\\',
                     r"\'",
                     # r'\0\',  # this could not be interpreted, i don't know how
                     '\\0\\',
                     r'\0 ',
                     r'\ 0',
                     r' \\',
                     r'\a\a',
                     r'\aa\a',
                     r'a\a\aa',
                     r'a\aa',
                     r"'",
                     r'"',
                     '\\',
                     r'\0\0',
                     r'\00\0',
                     r'\00\\0',
                     r'a\ca',
                     r'a\bba',
                     r'a\b ba',
                     r'a\b \ba'
                     ]
    
    for s in extended_test:
        test_palindrome(s, True)

if __name__=='__main__':

    print "Test simple palindrome: "
    test_simple_palindrome()
    print
    print "Test extended palindrome: "
    test_extended_palindrome()

    '''
    s = raw_input("Please input a string: ")
    test_palindrome(s, False)
    test_palindrome(s, True)
    '''

    print
    print "Test making a palindrome: "
    make_tests = [' ', '', 'a', 'ab', 'abc', 'aba' ]
    for i in make_tests:
        make_palindrome(i)
