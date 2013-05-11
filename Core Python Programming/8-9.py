# 8-9: fibonacci

def getNthFib(n):
    a = 1
    b = 1
    if (n==1):
        return a
    elif (n==2):
        return b

    i = 2
    while(i<n):
        a, b = b, a+b
        i += 1
    return b


if __name__=='__main__':
    for i in range(1,100):
        print "%d: %d"%(i,getNthFib(i))
