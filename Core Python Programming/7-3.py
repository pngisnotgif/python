# 7-3

dict1 = {'1':1, '123':2, 'a':3, '1a':4, 'abc':5}
print 'In keys order: '
for i in dict1.keys():
    print i,
print

print 'In alphabetical order:'
for i in sorted(dict1.keys()):
    print i,
print

print 'Keys and values in alphabetical order:'
for i in sorted(dict1.keys()):
    print i,':', dict1[i]
print

print 'Keys and values in alphabetical order of values:'
for i in reversed(sorted(dict1.values())):
    print ':', i # how to sort in value order?
print
