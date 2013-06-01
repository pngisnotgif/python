# 9-19

import random
import os

filename = '9-19.bin'

def createFile(charByte, times, fileLen):
    f = open(filename,'wb')
    charPos = random.sample(range(fileLen), times ) # generate 'times' different positions
    for i in range(fileLen):
        if i not in charPos:
            done = False
            while not done:
                ch = random.randint(0,255)
                if ch != charByte:
                    f.write(chr(ch))
                    done = True
        else:
            f.write(chr(charByte))
    f.close()

# from 9-18.py
def findChar(charIndex, filename):
    c = chr(charIndex)
    sum_c = 0
    for line in open(filename,'rb'):    # should be binary format
        sum_c += line.count(c)

    return sum_c

if __name__=='__main__':
    char = '\\' # should not use special char likd '\n'(2 bytes)
    charByte = ord(char)
    # charByte = 0
    times = 5
    file_len = 100
    for i in range(100):
        createFile(charByte, times, file_len)
        t = findChar(charByte, filename)
        if t!=times:
            print 'error in %d tries.'%(i)
            raw_input()
    print 'all files tested OK.'
    
