
# 6-5

num_str = raw_input('Enter a number:')

num_num = int(num_str)

fac_list = range(1, num_num+1)
print "BEFORE:"+`fac_list`

set_fac = set(fac_list)
i = 0

while i<len(fac_list):
    if num_num % fac_list[i] == 0:
        del fac_list[i]
    else:
        i = i + 1
    # print 'now i=%d'%i, fac_list

print "AFTER:"+str(fac_list)

print "Factors of %d are: "%num_num, str(list(set_fac-set(fac_list)))
