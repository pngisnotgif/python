# 6-13

import string
def atoc(s):
    '''
        the condition including expression like '1+j+5' is not considered.
    '''
    s.lower()
    legal_chars = string.digits + 'e.+-()'
    
    image_index = s.find('j')
    # print image_index
    if image_index == len(s)-1: # j in the end
        for i in range(image_index-1, -1, -1):
            if s[i] == ')':
                left_bracket = s.rfind('(')
                if left_bracket>0:
                    image = s[left_bracket-1:image_index]
                    real = s[:left_bracket-1]
                else:
                    image = s[:image_index]
                    real = 0
                break
            else:
                if s[i] not in (string.digits+'.'):
                    if i != (image_index - 1 ):
                        image = s[i:image_index]
                    else:
                        if s[image_index]=='-':
                            image = -1
                        else:
                            image = 1
                    real = s[:i]
                    if not real:
                        real = 0
                    break
        else:
            image = 1
            real = 0
    elif image_index == -1: # no j in expression
        real = s
        image = 0
    else:   # j in first part
        real = s[image_index+1:]
        image = s[:image_index]
        if image == '-':
            image = -1
        else:
            image = 1

    # print "(%s,%s)"%(real, image)
    return complex(float(real),float(image))

if __name__=='__main__':
    tests = ['1+2j', '1j+2','5','j','-1.23e+4-5.67j','-j-5','-0.1j',
             # '1.23e-4-(2.34e+5)j',    # this cannot be transformed using complex()
             # '-1.23e+4j',   # this is wrong, cause 'e' is not treated especially
             # '(-1.23e+4)j' # '()'cannot be transformed using complex()
             ]
    for i in tests:
        print atoc(i)

            
        
