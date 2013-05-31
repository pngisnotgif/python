# 9-16: line words processing

import string

def trunc(filename, src_str, boundary=80):
    l = src_str
    while (len(l)>boundary):
        space_pos = l.rfind(' ', 0, boundary-1)
        if (space_pos > -1):
            truncated = l[space_pos+1:] # leave space in the current line for appearance
            l = l[:space_pos+1]
        else:
            truncated = l[boundary:]
            l = l[:boundary]
            
        filename.write(l)
        if truncated:
            filename.write('\n')    # insert ENTER between lines
        l = truncated

    if truncated:
        filename.write(truncated)
        # filename.write('\n')      # last line contains an ENTER already
    
def processing(filename):
    try:
        f = open(filename,'r')
    except IOError:
        print 'file %s not found'%(filename)
        return

    lines = f.readlines()
    f.close()

    f_out = open(filename+'.post', 'w')
    for l in lines:
        if len(l)>80:
            trunc(f_out,l)
        else:
            f_out.write(l)

    f_out.close()
    
    
if __name__=='__main__':
    filename = '9-16.txt'
    processing(filename)
