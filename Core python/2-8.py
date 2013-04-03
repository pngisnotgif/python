
# 2-8
aList = [1,2,3,4,5]
aTuple = (1,2,3,4,5)

count = 0
aListSum = 0
aTupleSum = 0
while count<5:
    aListSum += aList[count]
    aTupleSum += aTuple[count]
    count += 1

print aListSum,'\n', aTupleSum

aListSumFor = 0
for i in aList:
    aListSumFor += i
print aListSumFor

aTupleSumFor = 0
for i in aTuple:
    aTupleSumFor += i
print aTupleSumFor
    
print 'Now plz enter 5 numbers: '
aNewList = []
aNewListSum = 0
for i in range(5):
    num = int(raw_input('[%d]-->'%(i+1)))
    aNewList.append(num)
    aNewListSum += aNewList[i]
print aNewListSum

# answer found in Stack Overflow : way creating tuple from user.
print 'Now again enter 5 interegers using comma as seperator.'
aNewTuple = tuple(int(x.strip()) for x in raw_input().split(','))
aNewTupleSum = 0
for i in aNewTuple:
    aNewTupleSum += i
print aNewTupleSum
