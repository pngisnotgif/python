# 7-13

import random

listA = [random.randint(0,10) for x in range(10)]
setA= set(listA)
print 'set A: ', setA

listB = [random.randint(0,10) for x in range(10)]
setB= set(listB)
print 'set B: ', setB

# using set operator:
print 'A|B = ', setA | setB
print 'A&B=', setA & setB

''' using set method: 
print 'A|B = ',setA.union(setB)
print 'A&B=', setA.intersection(setB)
'''


    
