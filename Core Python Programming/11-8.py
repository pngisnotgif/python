# -*- coding: utf-8 -*-

# 11-8

def isLeapYear(year):
    if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
        return True
    else:
        return False

if __name__=='__main__':
    # 测试闰年判断
    testYear = [1900, 2000, 2004, 2008, 2009, 2010, 2011, 2012, 2013]
    for i in testYear:
        print i,':',isLeapYear(i)
    print

    # 使用filter
    yearSeq = range(1980,2020)
    yearSeq.append(1900)
    yearSeq.append(1904)
    yearSeq.sort(reverse=True)
    leapYear = filter(isLeapYear, yearSeq)
    print '闰年：',leapYear

    # 使用list comprehension
    lYear = [x for x in yearSeq if isLeapYear(x)]
    print '闰年：',lYear
