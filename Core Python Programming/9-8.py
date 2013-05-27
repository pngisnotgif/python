# 9-8

module_name = 'os'

module = __import__(module_name)

module_dict = module.__dict__

count = 25

# how to sort in type?
# for i in sorted(module_dict.keys(), key=lambda x:str(type(x))):

for i in sorted(module_dict.keys()):
    print 'Name: ', i, 'Type:', type(module_dict[i]), 'Value:', module_dict[i]
    count -= 1
    if count<=0:
        count = 25
        raw_input()
