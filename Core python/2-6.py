
# 2-6: condition judgement

print 'Please enter a number:'
num =int(raw_input())

str_prefix = '%d is '%(num)
if num>0:
    print str_prefix+'positive'
elif num==0:
        print str_prefix+'zero'
else:
        print str_prefix+'negetive'

