# 6-17

def myPop(someList):
    del someList[len(someList)-1]
    return someList

aList = []
aList.append('1')
aList.append(['2','3'])
aList.append('4')
print 'Before: ', aList
print 'After: ', myPop(aList)
