# 6-3

s = raw_input("Please input a series of integral numbers, using SPACE to seperate: \n> ")

import string
ranges = string.digits + ' '

for c in s:
    if c not in ranges:
        print "You may have entered non-digit characters."
        # HOW to terminate? 
        exit()
        break

list_input = s.split()

import copy
list_copy = copy.deepcopy(list_input)

nums = []
for i in list_input:
    nums.append(int(i))

print "Sorted result:"
print "  BIG-->SMALL: ",
nums.sort()
nums.reverse()
for i in nums:
    print i,
print

list_copy.sort()
list_copy.reverse()

print "  alphabetically(reverse order): ",
for i in list_copy:
    print i,
print

    


