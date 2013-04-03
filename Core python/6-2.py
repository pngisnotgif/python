''' a script that test whether a string is legal id string:
 which is started with an alphabet or slash.

'''


def test_id_string(str_input):
    
    # str_input = raw_input('Please input a string: ')

    len_str = len(str_input)

    import string
    alpha = string.letters
    nums = string.digits
    legal_seq = alpha + nums + '_'

    import keyword
    key = keyword.kwlist

    if len_str==0 :
        print 'WORNG: zero-lengthed string("%s").'%(str_input)
    elif str_input[0] in nums:
        print 'WORNG: first character"%s" in "%s" is a digit. '\
              %(str_input[0], str_input)
    elif str_input[0] not in legal_seq:
        print 'WORNG: first character"%s" in "%s" is not letter \
or digit or slash("_"). '%(str_input[0], str_input)

    # elif keyword.iskeyword(str_input):    # use this expression is also OK, but not so efficient
    elif str_input in key:
        print 'WORNG: "%s" is conflict with python keywords'%(str_input)
    else:
        for every_letter in str_input[1:]:
            if every_letter not in legal_seq:
                print 'WORNG: illegal character "%s" included in "%s".'%(every_letter, str_input)
                break
        else:
            print 'CORRECT: "%s" is a legal string for an varible name'%(str_input)
            global correct_count
            correct_count += 1

                                                
if __name__ == '__main__':

    test_cases = ['', ' ', 'a', '1', '_', '123', 'abc' ,'__', 'a1', '1a',
                  '1_','_1', '_ab1', 'is', ' is', 'is ', 'if', 'if_al',
                ]
    
    correct_count = 0
    amount = len(test_cases)
    i = 0
    for testcase in test_cases:
        i += 1
        print '[%d]'%(i),
        test_id_string(testcase)
        
    print '\n Summary: %d correct VS %d wrong in all the %d testcase(s).'\
          %(correct_count, amount-correct_count, amount)
 
