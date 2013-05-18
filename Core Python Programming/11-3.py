# 11-3

def max2(a, b):
    if a>=b:
        return a
    else:
        return b

def min2(a, b):
    if a<=b:
        return a
    else:
        return b

def my_func(func, *seq):
    l = len(seq)
    
    if l==0:
        return 'None'

    if l==1:
        return seq[0]

    res = seq[0]
    for i in range(1,l):
        res = func(res, seq[i])

    return res

def my_max(*seq):
    return my_func(max2, *seq)

def my_min(*seq):
    return my_func(min2, *seq)
    
print max2(4,8)
print min2(4,8)
print my_max()
print my_max(1)
print my_max(1,2)
print my_max(1,3,2)
print my_min(1,3,2)
print my_min('1','2','10')
print my_max('1','2','10','11','a')
