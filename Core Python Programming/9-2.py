# 9-2

def cat(filename, n):
    try:
        f = open(filename,'r')
    except IOError:
        print "file %s does not exist or could not be opened."%(filename)
        return

    count = n
    if count>0:
        for i,line in enumerate(f):
            print i+1,':',line,
            count -= 1
            if count <= 0:
                break

    print
    f.close()
    

if __name__=='__main__':
    filename = '9-2.py'

    cat(filename, 0)
    cat(filename, 1)
    cat(filename, 5)
    cat(filename, 50)
    
