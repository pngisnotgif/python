# 9-6

def diff(file1, file2):
    '''
        Compare two files and print the first place they differs.
    '''
    try:
        f1 = open(file1)
        lines1 = f1.readlines()
    except IOError:
        print "file: '%s' open failed."%(file1)
        return
    finally:
        f1.close()

    try:
        f2 = open(file2)
        lines2 = f2.readlines()
    except IOError:
        print "file: '%s' open failed."%(file2)
        return
    finally:
        f1.close()

    same = True
    row = 0
    col = 0
    # f1 is not empty
    for i,line in enumerate(lines1):
        for j in range(len(line)):
            try:
                if line[j] != lines2[i][j]:
                    same = False
                    row, col = i, j
                    break
                    # return # this can directly end 'for'
            except IndexError:
                same = False
                row, col = i, j
                break
            if not same :
                break
        if not same:
            break

    # In case of that f1 is empty but f2 isn't.
    # This time, statement in 'for i'is not executed.
    if same and len(lines1)==0 and len(lines2)!=0:
        same = False
        
    if same:
        print "file '%s' and '%s' are the same."%(file1, file2)
    else:
        print "file '%s' and file '%s' differ in line:%d col:%d."\
                          %(file1, file2, row+1,col+1)
    
if __name__=='__main__':
    filename1 = '9-6.py'
    filename2 = '9-1.py'

    diff(filename1, filename2)
    diff(filename1, filename1)
    diff(filename1, '')
    diff('empty_file.txt', filename1)
    diff(filename1, 'empty_file.txt')
