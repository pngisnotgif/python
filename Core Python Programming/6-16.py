# 6-16

def print_matrix(m):
    # if this function is in matrix_add(), it works. I don't know why.
    row, col = len(m), len(m[0])
    print '[ ',
    for x in range(row):
        print '[',
        for y in range(col):
            print (a[x][y]+b[x][y]),
            if y < col-1:
                print ',',
        print ']'
    print ']'
    
def matrix_add(a,b):
    row_a, column_a = len(a), len(a[0])
    row_b, column_b = len(b), len(b[0])
    if row_a == row_b and column_a == column_b:
        res = (( (a[x][y]+b[x][y]) for x in range(row_a) ) for y in range(column_a))

    return res # not finished, this is a generator.
    

def matrix_mul(a,b):
    pass

if __name__=='__main__':

    M = [ [1,1,1],
          [1,1,1],
          [1,1,1]
        ]
    N = [ [2,2,2],
          [2,2,2],
          [2,2,2]
        ]
    
    test_matrix = [

        ]

    print "M+N="
    # print_matrix(matrix_add(M,N))
    print matrix_add(M,N)   # problem: generator don't have method len()
                            # I'll leave this script for later solution.
