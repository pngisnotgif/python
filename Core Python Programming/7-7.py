# 7-7

def revert_dict(dt):
    ret_dict = {}
    for d in dt:
        key = d
        value = dt[d]
        try:
            ret_dict[value] = key
        except TypeError:
            print '\n original dict type error:', key, ':', value
    return ret_dict
    
if __name__=='__main__':
    test_dicts = [
        {'abc':1, 'a':'2', 5:'3ab'},
        {1:'a', '2':'b', '1':'c', 4:{'name':'value'}} # nested dict
        ]

    new_dicts = []
    for i in test_dicts:
        print i, '==>', # original dictionary
        new_dict = revert_dict(i)
        new_dicts.append( new_dict )
        print new_dict

