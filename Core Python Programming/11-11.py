# 11-11

def cleanFile(filename, override = False):
    '''
        Strip every line of file.

        If parameter 'override' equals to True, the original file will be overridden.
        Otherwise, a new file whose name with a suffix '.post' will be created.
    '''
    import os
    
    try:
        f = open(filename)
    except IOError:
        print "file '%s' open failed."%(filename)
        return
    
    lines = f.readlines()
    f.close()

    if not override:
        newFilename = filename + '.post'
    else:
        newFilename = filename

    try:
        f_write = open(newFilename,'w')
    except IOError:
        print "file '%s' created failed."%(f_write)
        return

    # using map
    # new_lines = map(lambda x:x.strip()+os.linesep, lines)

    # using list comprehension
    new_lines = [x.strip()+os.linesep for x in lines]
    
    f_write.writelines(new_lines)
    f_write.close()

if __name__=='__main__':
    fname = '11-11.py'
    cleanFile(fname)

    cleanFile(fname+'.post', True)

    cleanFile('empty_file.txt')
