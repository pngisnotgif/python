# 7-15

def doSetOperation( setA, setB, opr ):
    if opr=='in':
        if setA in setB:
            print '%s is in %s'%(setA, setB)
        else:
            print '%s is not in %s'%(setA, setB)
    elif opr=='not in':
        if setA not in setB:
            print '%s is not in %s'%(setA, setB)
        else:
            print '%s is in %s'%(setA, setB)
    elif opr=='&':
        print '%s & %s = %s'%(setA, setB, setA & setB)
    elif opr=='|':
        print '%s | %s = %s'%(setA, setB, setA | setB)
    elif opr=='^':
        print '%s ^ %s = %s'%(setA, setB, setA.symmetric_difference(setB))
    elif opr=='<':
        if setA < setB:
            print '%s IS strictly subset of %s'%(setA, setB)
        else:
            print '%s IS NOT strictly subset of %s'%(setA, setB)
    elif opr=='<=':
        if setA <= setB:
            print '%s IS subset of %s'%(setA, setB)
        else:
            print '%s IS NOT subset of %s'%(setA, setB)
    elif opr=='>':
        if setA > setB:
            print '%s IS strictly superset of %s'%(setA, setB)
        else:
            print '%s IS NOT strictly superset of %s'%(setA, setB)
    elif opr=='>=':
        if setA >= setB:
            print '%s IS subset of %s'%(setA, setB)
        else:
            print '%s IS NOT subset of %s'%(setA, setB)
    elif opr=='==':
        if setA == setB:
            print '%s == %s'%(setA, setB)
        else:
            print '%s != %s'%(setA, setB)
    elif opr=='!=':
        if setA != setB:
            print '%s != %s'%(setA, setB)
        else:
            print '%s == %s'%(setA, setB)

if __name__=='__main__':
    test_sets = [ ['',''],
                  ['1', '1 2 3'],
                  ['1 2 3', '1'],
                  ['1 2', '1 2'],
                  ['1 2 3', '2 3 4'],
                  ['1 2 3', '4 5'],
                  ["'1'", 'set(["1"]) 2 3'],
                  ['1', 'set("1") 2 3'] # not correct now, TODO later
        ]

    '''
    prompt = 'Please input set %s(using SPACE to seperate):'

    listA = raw_input(prompt%('A')).split()
    setA = set(listA)

    listB = raw_input(prompt%('B')).split()
    setB = set(listB)

    opr_prompt = 'choose operator from: in, not in, &, |, ^, <, <=, >, >=, ==, !=: '
    opr = raw_input(opr_prompt).strip()
    '''

    oprs = ['in', 'not in', '&', '|', '^', '<', '<=', '>', '>=', '==', '!=']

    for test in test_sets:
        setA = set(test[0].split())
        setB = set(test[1].split())
        for opr in oprs:
            doSetOperation( setA, setB, opr )
        print
    
