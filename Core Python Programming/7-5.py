#!/usr/bin/env python

# 7-5

# v1.1 - add timestamp
# v1.0 - from example 7.1

import time

db = {}

def save_timestamp(name):
    db[name]['timestamp'] = time.time()
    
def newuser():
    prompt = 'Login desired: '
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'Warning: name taken, try another login: '
            continue
        else:
            break
    
    pwd = raw_input('Passwd: ')
    db[name] = {}
    db[name]['pwd'] = pwd
    save_timestamp(name)

def olduser():
    name = raw_input('Login: ')
    pwd = raw_input('Passwd: ')
    passwd = db[name].get('pwd')
    if passwd == pwd:
        print 'Welcome back,', name, '!'
        if (time.time()- db[name]['timestrmp']) < 4*60*60:  # less than 4 hours
            print 'You already logged in at: %s.' \
                  %(time.strftime('%x %X',time.localtime(db[name]['timestamp'])))
            # change timestamp in seconds since the epoch to 9-tuple, and then to string
        save_timestamp(name)
    else:
        print 'Warning: login or passwd incorrect.'
    raw_input()

def showmenu():
    prompt ="""
        MENU
      ========
(N)ew User Login
(E)xisting User Login
(Q)uit

Enter choice: """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
                
            print 'You picked: [%s]'%choice
            
            if choice not in 'neq':
                print 'Warning: invalid option, try again.'
                raw_input()
            else:
                chosen = True

        if choice == 'q':
            done = True
            print 'Bye!'
        if choice == 'n':
            newuser()
        if choice == 'e':
            olduser()

if __name__=='__main__':
    showmenu()
