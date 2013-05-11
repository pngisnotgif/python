# 8-10

import string
def stat_word(str_in):
    vowels = 'aeiou'

    v = len([c for c in str_in.lower() if c in vowels])
    l = sum([len(c) for c in str_in if c in string.letters])
    c = l-v
    words = len(str_in.split())

    print 'in: %s'%(str_in)
    print 'vowels: %d'%(v)
    print 'consonants: %d'%(c)
    print 'words: %d'%(words)
    print
    
if __name__=='__main__':
    tests = [
        'This is a sentence.',
        'abcdefg hijklmn opq rst uvw xyz',
        'The quick brown fox jumps over the lazy dog.'
        ]

    for t in tests:
        stat_word(t)
    
