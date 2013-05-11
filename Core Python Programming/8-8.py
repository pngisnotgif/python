# 8-8: factorial

# using recursion 
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

if __name__=='__main__':
    for i in range(1,100):
        print "%d!=%d"%(i,factorial(i))
