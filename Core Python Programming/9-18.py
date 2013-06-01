# 9-18

def findChar(charIndex, filename):
    c = chr(charIndex)
    sum_c = 0
    for line in open(filename):
        sum_c += line.count(c)

    return sum_c
    
if __name__=='__main__':
    filename = '9-18.py'
    char = '_'
    index = ord(char)
    print "times of char '%s' in file '%s': %d"\
          %(char, filename, findChar(index, filename))
