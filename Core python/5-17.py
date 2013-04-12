# 5-17: generate random numbers.

import random

random.seed()

#n = random.randint(0,2**31-1)
N = random.randint(2,100)
aList = [random.randint(0,2**31-1) for x in range(N)]

print 'N = ' + str(N)
print 'Sample: \n' + str(aList)

m = random.randint(1,N)
aSubList = random.sample(aList, m)
print 'm = ' + str(m)
print 'source Sub-Sample: \n' + str(aSubList)

def sortMethod1(out=True):
    # using deep copy and sort method
    
    import copy
    sortedList = copy.deepcopy(aSubList)
    sortedList.sort()
    if out == True:
        print 'sorted Sub-Sample: \n' + str(sortedList)


def sortMethod2(out=True):
    
    import copy
    sortedList = copy.deepcopy(aSubList)

    lenOfSubList = len(sortedList)
    for i in range(lenOfSubList-1):
        for j in range(lenOfSubList):
            if j<=i: continue
            else:
                a = sortedList[i]
                b = sortedList[j]
                if a>b :
                    sortedList[i], sortedList[j] = b, a
    if out==True:
        print 'another sorted Sub-Sample: '
        print sortedList

if __name__=='__main__':
    from timeit import Timer
    
    t1 = Timer("sortMethod1(False)","from __main__ import sortMethod1")
    t2 = Timer("sortMethod2(False)","from __main__ import sortMethod2")
    testTimes = 10000
    print 'sortMethod1() time: %f'%(t1.timeit(testTimes))
    print 'sortMethod2() time: %f'%(t2.timeit(testTimes))

# sortMethod1()
# sortMethod2()
