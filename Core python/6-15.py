# 6-15

import copy

def dayStr_to_int(day):
    '''
        @day in format: MM/DD/YYYY
        @return [month, day, year] in integer
    '''
    return [ int(x) for x in day.split('/') ]

def isLeapYear(year):
    return (year % 4 == 0 and year % 100 !=0 or year % 400 == 0)
    
def days_between(day1, day2):
    days_of_year = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # insert 0 to let month equals list index
    days_of_common_year = sum(days_of_year)
    
    m1, d1, y1 = dayStr_to_int(day1)
    m2, d2, y2 = dayStr_to_int(day2)

    # swap day if day1 later than day2
    if (y1>y2) or (y1==y2 and m1>m2) or (y1==y2 and m1==m2 and d1>d2):
        m1, d1, y1, m2, d2, y2 = m2, d2, y2, m1, d1, y1
        
    days = 0
    if y1==y2:  # same year
        if isLeapYear(y1):
            days_of_year[2] += 1
            print 'Same year: Leap year %d'%(y1)
        if m1 != m2:
            days += days_of_year[m1] - d1
            for i in range(m1+1,m2,1):
                days += days_of_year[i]
            days += d2
        else:
            days += d2 - d1
    else:
        days_of_year_copy = copy.copy(days_of_year) # need copy,
            # or days_of_year may change accroding to days_of_year_copy
        if isLeapYear(y1):
            days_of_year_copy[2] += 1
            print 'Leap year %d'%(y1)
            # print days_of_year
            
        days += days_of_year_copy[m1] - d1
        for i in range(m1+1,12+1,1):
            days += days_of_year_copy[i]
        days += (y2-y1-1) * days_of_common_year + (y2-y1-1)/4
        # bug here, how many leap years between? 

        days_of_year_copy2 = copy.copy(days_of_year)
        # print days_of_year_copy2
        if isLeapYear(y2):
            days_of_year_copy2[2] += 1
            print 'Leap year %d'%(y2)
        for i in range(1,m2,1):
            days += days_of_year_copy2[i]
        days += d2

    return days
    

if __name__=='__main__':
    test_days_between = [
                    ['01/01/2013','01/02/2013'],
                    ['01/01/2013','01/01/2013'],
                    ['01/01/2013', '02/01/2013'],
                    ['01/01/2013', '12/31/2013'],
                    ['01/01/2000', '03/1/2000'],
                    ['03/01/2000', '4/1/2000'],
                    ['01/01/2013', '01/01/2014'],
                    ['01/01/2013', '02/01/2014'],
                    ['2/2/2014','3/1/2015'],
                    ['1/1/2000', '1/1/2002'],
                    ['1/1/2000', '1/1/2008'],
                    ['1/1/1983','1/1/2013'],
                    ['2/13/1983','4/21/2013'],
                    ['1/1/1000','1/1/1900'],    # test leap year
                ]
    for d1, d2 in test_days_between:
        print "Days between %s and %s : %d "%(d1, d2, days_between(d1, d2))
