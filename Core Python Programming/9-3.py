# 9-3 get lines of file

def lines(filename):
    try:
        f = open(filename)
    except IOError:
        print 'file open error: %s.'%(filename)
        return -1

    ret = len(f.readlines())
    f.close()
    return ret

if __name__=='__main__':
    filenames = ['empty_file.txt','9-3.py','error.txt']

    for i in filenames:
        l = lines(i)
        if l>=0:
            print "Lines of file '%s': %d"%(i, lines(i))

