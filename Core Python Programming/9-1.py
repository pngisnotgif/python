# 9-1: file filtering

def filterFile(filename, omitOtherSharps = False):
    try:
        f = open(filename,'r')
    except IOError:
        print 'file: %s does not exist.'%(filename)
        return

    for line in f:
        if line[0]=='#':
            continue
        else:
            if not omitOtherSharps or '#' not in line:
                print line, # python will insert a "return" in every line
            else:
                # print line[:line.index('#')],'\n',  # this will insert a space between
                print line[:line.index('#')]

    f.close()

if __name__=='__main__':
    filename = r'9-1.py'
    print 'After deleting the "#" sign in front of every line:'
    filterFile( filename )

    print '\nAfter deleting all the "#" sign: '
    filterFile( filename,True )
