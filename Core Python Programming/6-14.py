# 6-14
# Rochambeau

import random

debug = True
# debug = False

def Rochambeau(n):
    text = {0:'Cloth', 1:'Scissor', 2:'Stone'}
    win = 0
    lose = 0
    draw = 0
    
    i = 0
    while i<n:
        mac = random.randrange(0,3,1)

        if debug:
            human = random.randrange(0,3,1)
        else:
            human = int(raw_input('Your choice(0-Cloth, 1-Scissor, 2-Stone):'))
            
        if human>=3 or human <0:
            print "Wrong input."

        if not debug:
            print "You: %s   Computer: %s "%(text[human],text[mac]),
        
        r = (mac - human) % 3        
        if r == 1 : # or r == -2:
            if not debug:
                print "You lose! "
            lose += 1
        elif r == 2 : # or r == -1:
            if not debug:
                print "You win! "
            win += 1
        else: # r==0
            if not debug:
                print "Draw! "
            draw += 1

        i+=1

    print "Sumary: win=%d, lose=%d, draw=%d. Sum=%d "%(win, lose, draw, i)

if __name__ == '__main__':
    if debug:
        Rochambeau( 100000 )
    else:
        Rochambeau( 5 )

