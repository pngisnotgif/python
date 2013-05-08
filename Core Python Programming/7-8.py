# 7-8

if __name__=='__main__':
    test_data = [
        {'name':'abc', 'id':1},
        {'name':'1', 'id':2},
        {'name':'a1', 'id':3},
        {'name':'2', 'id':20},
        {'name':'a', 'id':5}
        ]

    from operator import itemgetter
    print 'Order by Name:'
    for i in sorted(test_data, key=itemgetter('name')): # using key, not index
        print "name: '", i['name'], "', id:", i['id']

    print 'Order by ID: '
    for i in sorted(test_data, key=itemgetter('id')):
        print i

    print 'Order by ID, using lambda expression: '
    for i in sorted(test_data, key=lambda x:x['id']):
        print i
