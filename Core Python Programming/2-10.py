
# 2-10
# I changed this exercise to guess a number using random and while, if statement.

import random

random.seed()
targetNum = random.randint(1,100)
print "Now let's guess a number between 1 and 100."
foundIt = False
times = 0
while foundIt != True:
    num = int(raw_input('==> '))
    times += 1
    if num<targetNum:
        print 'Try bigger. '
    elif num>targetNum:
        print 'Try smaller.'
    else:
        print 'You guessed it in %d times! \n'%(times)
        foundIt = True

        
