#!/usr/bin/env python

# 7-5

# v1.2 - add sub-menu: administrate(del account, and list users)
# v1.1 - add timestamp
# v1.0 - from example 7.1

import time

db = {}

def save_timestamp(name):
    db[name]['timestamp'] = time.time()

def get_last_login_time(name):
    return db[name]['timestamp']
    
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
        if (time.time()- get_last_login_time(name)) < 4*60*60:  # less than 4 hours
            print 'You already logged in at: %s.' \
                  %(time.strftime('%x %X',time.localtime(get_last_login_time(name))))
            # change timestamp in seconds since the epoch to 9-tuple, and then to string
        save_timestamp(name)
    else:
        print 'Warning: login or passwd incorrect.'
    raw_input()

def delUser():
    if db.keys():
        prompt = 'Login to be deleted: '
        name = raw_input(prompt)
        if name in db:
            print 'Detail of %s: \n'%(name), db[name]
            confirm = raw_input('Delete this account? Y or N? ').strip().lower()
            if confirm == 'y':
                del db[name]
                print 'Account: %s is deleted.'%(name)
            else:
                print 'No account is deleted.'
        else:
            print 'No such an account.'
    else:
        print 'Empty accounts.'
    raw_input()

def listAllUser():
    if db.keys():
        for user in db:
            print 'name:', user,
            print 'password:', db[user]['pwd']
    else:
        print 'No accounts.'
    raw_input()

def administrate():
    '''
        sub-menu of main menu.

    '''
    
    prompt = '''
        Administrate
        ============
(D)elete an account
(L)ist all acounts
(R)eturn

Enter your choice: '''

    ret = False
    while not ret:
        try:
            choice = raw_input(prompt).strip()[0].lower()
        except (EOFError, KeyboardInterrupt):
            choice = 'r'    # how to directly return to showmenu()?

        print 'You picked: [%s]'%choice
        if choice not in 'dlr':
            print 'Warning: invalid option, try again.'
            raw_input()
        else:
            if choice == 'd':
                delUser()
            if choice == 'l':
                listAllUser()
            if choice == 'r':
                ret = True

    
def showmenu():
    prompt ="""
        MENU
      ========
(N)ew User Login
(E)xisting User Login
(A)dministrate
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
            
            if choice not in 'neqa':
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
        if choice == 'a':
            administrate()

if __name__=='__main__':
    showmenu()
