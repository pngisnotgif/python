# initdata.py

# initialize date to be stored in files, pickles, shelves.

# records
bob = {'name':'Bob Smith', 'age':42, 'pay':30000, 'job':'dev'}
sue = {'name':'Sue Jones', 'age':45, 'pay':40000, 'job':'mus'}
tom = {'name':'Tom',       'age':50, 'pay':0,     'job':None}

# datebase
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':      # when run as a script
    for key in db:
        print key,'=>\n', db[key]
