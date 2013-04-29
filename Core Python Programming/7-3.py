# 7-3

dict1 = {'1':1, '123':2, 'a':3, '1a':4, 'abc':5}
print 'In keys order: '
for i in dict1.keys():
    print i,
print
print

print 'In alphabetical order:'
for i in sorted(dict1.keys()):
    print i,
print
print

print 'Keys and values in alphabetical order:'
for i in sorted(dict1.keys()):
    print i,':', dict1[i]
print

# sorting method, see: http://wiki.python.org/moin/HowTo/Sorting/
print 'Keys and values in alphabetical order of values:'

# Method 1: using operator.itemgetter
from operator import itemgetter
for i,j in sorted(dict1.items(), key=itemgetter(1), reverse=True):

# or Method 2: using lambda statement    
# for i,j in sorted(dict1.items(), key=lambda dict1:dict1[1], reverse=True):

    print "'%s':%d"%(i,j) # how to sort in value order?
print
