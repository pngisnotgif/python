# 9-4 : more()

def more(fname, lines=25):
    try:
        f = open(fname)
    except IOError:
        print 'open file error: %s'%fname
        return

    line = lines
    for i in f:
        print i,
        line -= 1
        if line <= 0:
            raw_input('<Press any key to continue.>')
            line = lines

if __name__=='__main__':
    filename = '7-9.py'
    more(filename)
    
    
