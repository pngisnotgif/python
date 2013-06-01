#!/usr/bin/env python

# 7-5, and 9-12

# v1.7 - add admin account support, and save db in pickle
# v1.6 - merge newuser() and olduser()
#        fix bug: empty choice string causes exception
# v1.5 - abandon signs and whitespaces for name
# v1.4 - ignore case of name
# v1.3 - encrypt user's password
# v1.2 - add sub-menu: administrate(del account, and list users)
# v1.1 - add timestamp
# v1.0 - from example 7.1

# TODO: using Tkinter to make an UI.

import time
import hashlib
import string
import pickle

db = {}
db_filename = 'login.pkl'
def loadDB():
    global db
    try:
        db_file = open(db_filename,'r')
    except IOError:
        print 'open file %s failed.'%(db_filename)
        return
    
    if db_file:
        db = pickle.load(db_file)
        db_file.close()

def saveDB():
    global db
    
    db_file = open(db_filename,'w')
    pickle.dump(db, db_file, pickle.HIGHEST_PROTOCOL)

def save_timestamp(name):
    db[name]['timestamp'] = time.time()

def get_last_login_time(name):
    return db[name]['timestamp']

def check_name(name):
    legal_chars = string.digits + string.letters 
    
    for c in name:
        if c not in legal_chars:
            return False

    return True

def check_and_lower_name(prompt):
    name_legal = False
    while not name_legal:
        name = raw_input(prompt)
        if check_name(name):
            name_legal = True
        else:
            print 'Warning: no signs and space are allowed.'

    return name.lower()

admin_name = 'admin'
admin_init_pwd = 'admin'
def check_and_create_admin():
    if not db.has_key(admin_name):
        db[admin_name]={}
        pwd = hashlib.md5( admin_init_pwd ).hexdigest()
        db[admin_name]['pwd'] = pwd
        save_timestamp(admin_name)    
    
def newuser(name):
    first_time = True
    
    prompt = 'Login desired(ignore case): '
    while True:
        if not first_time:
            name = check_and_lower_name(prompt)

        first_time = False            
        if db.has_key(name):
            prompt = 'Warning: name taken, try another login: '
            continue
        else:
            break
    
    p = raw_input('Passwd: ')
    db[name] = {}

    pwd = hashlib.md5(p).hexdigest()  # using md5 to generate password.
    db[name]['pwd'] = pwd
    
    save_timestamp(name)

def olduser(name):
    p = raw_input('Passwd: ')
    pwd = hashlib.md5(p).hexdigest()    # check password using md5
    passwd = db[name].get('pwd')
    if passwd == pwd:
        print 'Welcome back,', name, '!'
        if (time.time()- get_last_login_time(name)) < 4*60*60:  # less than 4 hours
            print 'You already logged in at: %s.' \
                  %(time.strftime('%x %X',time.localtime(get_last_login_time(name))))
            # change timestamp in seconds since the epoch to 9-tuple, and then to string

            save_timestamp(name)
    else:
        print 'Warning: passwd incorrect.'

def login():
    prompt = 'Login: '

    done = False
    while not done:
        name = check_and_lower_name(prompt)

        if name not in db:
            print 'No such an account.'
            choice = raw_input('Will you register a new user? (Y/N) ').strip().lower()
            if choice == 'y':
                newuser(name)
                done = True
            else:
                print 'Re-enter the account:'
        else:
            olduser(name)
            done = True
        
    raw_input()

def delUser():
    if db.keys():
        prompt = 'Login to be deleted: '
        name = check_and_lower_name(prompt)      
                
        if name in db:
            if name == 'admin':
                print 'admin could not been deleted.'
            else:
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
            print 'name:', user,',',
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
            choice = 'r'
        except IndexError:
            continue

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
(S)ign in
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
            except IndexError:
                continue
                
            print 'You picked: [%s]'%choice
            
            if choice not in 'saq':
                print 'Warning: invalid option, try again.'
                raw_input()
            else:
                chosen = True

        if choice == 'q':
            done = True
            print 'Bye!'
        if choice == 's':
            login()
        if choice == 'a':
            administrate()

if __name__=='__main__':
    loadDB()
    check_and_create_admin()
    showmenu()
    saveDB()
