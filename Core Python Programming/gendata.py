# gendata.py
# 15-16

from random import randint, choice
from string import lowercase
from sys import maxint
from time import ctime

doms = ('com', 'edu', 'net', 'org', 'gov')

filename = 'redata.txt'
f = open(filename, 'w')

for i in range(randint(5, 10)):
    dtint = randint(0, maxint-1)    # pick date
    dtstr = ctime(dtint)            # date string

    shorter = randint(4, 7)         # login shorter
    em = ''
    for j in range(shorter):        # generate login
        em += choice(lowercase)

    longer = randint(shorter, 12)   # domain longer
    dn = ''
    for j in range(longer):         # create domain
        dn += choice(lowercase)

    out_str = '{}::{}@{}.{}::{}-{}-{}'.format(
        dtstr, em, dn, choice(doms), dtint, shorter, longer)
    
    # print out_str     # output to stdout
    
    f.write(out_str)    # output to file
    f.write('\n')

f.close()
    
