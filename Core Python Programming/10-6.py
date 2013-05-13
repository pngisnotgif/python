# 10-6

def my_open(filename, access_mode='r', buffering=-1):
    try:
        f = open(filename, access_mode, buffering)
    except (IOError, ValueError):
        f = None

    return f

if __name__=='__main__':
    test_cases = [
        [r'd:\abc.txt'],
        [r'd:\a.txt'],              # wrong filename
        [r'd:\abc.txt','w'],
        [r'd:\abc.txt','r',1],
        [r'd:\abc.txt','rb',1],
        [r'd:\abc.txt','rab',0],    # wrong access mode
        ]

    for i in test_cases:
        name = i[0]
        
        if len(i)>=2:
            mode = i[1]
        else:
            mode = 'r'
            
        if len(i)>=3:
            buf = i[2]
        else:
            buf = -1
            
        f = my_open(name,mode,buf)
        if f:
            print 'file handle created: ',f
        else:
            print 'file not opened.'
    
