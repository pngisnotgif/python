# 9-15

import sys
import os

def copy_file(from_file, to_file):

    f2 = open(to_file,'a')
    
    for l in open(from_file):
        f2.writelines(l)

    f2.close()
    
if __name__=='__main__':
    args = sys.argv[1:]
    if args:
        from_file = args[0]
        to_file = args[1]
    else:
        from_file = '9-15.py'
        to_file = '9-15.txt'

    copy_file(from_file, to_file)
    print 'copy finished.'
