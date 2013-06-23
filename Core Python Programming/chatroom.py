# chatroom: 13-12

import time
import random

class Message(object):
    '''
        message class
    '''

    def __init__(self, sent, rec, msg=None):
        self.msg_str = msg
        self.sent = sent
        if rec == 'all':
            self.broadcast = True
            self.recipient = 'all'
        else:
            self.broadcast = False
            self.recipient = rec
        self.time = time.time()

    def __str__(self):
        return self.msg_str

    def show(self):
        return self.__str__()

class User(object):
    '''
        user class
    '''

    def __init__(self, nickname):
        self.name = nickname
        self.messages = {} # this is a instance-bound attribute
        
        print '%s joined in the chatroom.'%(nickname)
        time.sleep(1)

    def __str__(self):
        return self.name
    
    def invite(self, room, person):  # invite someone to some room
        print "{} sent invitation to {} for joining '{}'".format(self, person, room)
        time.sleep(1)

    def accept(self, room, inviter): # accept invitation
        print "{} accepted invitation from {} to join '{}'"\
              .format(self, inviter, room)
        time.sleep(1)

    def decline(self, room, inviter):
        print "{} declined invitation from {} to join '{}'"\
              .format(self, inviter, room)
        time.sleep(1)

    def say(self, listener, words, room=None): 
        '''
            Say something to someone(listener).

            If room is None, chat in current room.
        '''

        if listener != 'all' and listener not in room.get_user_list():
            print "WARN: %s is not allowed to talk to %s: %s"%(self, listener, words)
            return

        msg = Message(msg = words, sent = self, rec = listener)
        if room not in self.messages:
            self.messages[room] = []
        self.messages[room].append(msg)
        
        print "{} says '{}' to {}.".format(self, words, listener)
        time.sleep(1)
        
        if listener=='all':
            room.broadcast(self, words)

    def show_messages(self, room):
        'show messages in specified room'
        assert room in self.messages

        print '  msgs of %s in %s:'%(self, room)
        i = 0
        for msg in self.messages[room]:
            i += 1
            print '\t',i,':',msg
        time.sleep(1)
    
    def show_all_messages(self):
        'show messages in every room.'

        print 'msgs of %s in ALL rooms:'%(self)
        for rm in self.messages:
            self.show_messages(rm)
        time.sleep(1)


class Ad(object):
    '''
        Advertisement class
    '''

    def __init__(self, ad = None):
        if ad is None:
            self.ad = 'This is an ad.'
        else:
            self.ad = ad

    def __str__(self):
        return self.ad

class AdPresenter(object):

    ad_list = ['Python supported this chatroom.',
               'Github stored source code.',
               'Programs written with Mac Air.',
               'Lenovo also supperted all the work.']
    
    def show(self):
        ad_content = str(random.sample(self.ad_list,1)[0])
        ad = Ad(ad_content)
        print ad
    

class Room(object):

    rooms = 0 # count of rooms(instances)

    def __init__(self, rm_name = None):
        'create a room with a name.'
        
        self.rooms += 1
        
        if not rm_name is None: # room name
            self.name = rm_name
        else:
            self.name = 'rm' + str(self.rooms)

        self.usrs = []  # user lists of this room
        self.ad = AdPresenter() # ads in this room

        print 'Room "%s" is created.'%(rm_name)
        time.sleep(1)

    def __str__(self):
        return 'Room %s'%(self.name)

    def get_user_list(self):
        return self.usrs

    def join(self, user):
        "a new user joins in this room"
        
        print "User %s joined in room %s"%(user, self)
        if user not in self.usrs:
            self.usrs.append(user)
        time.sleep(1)
   
    def invite(self, inviter, invitee):
        "a user invites someone to this room"
        
        inviter.invite(self.name, invitee)
    
    def display_all_messages(self):
        "Display all messages in this room according to time order."

        print "Messages in %s:"%(self)
        
        msgs = []

        # search messages from user's message dictionary in this room
        for user in self.usrs:
            if self in user.messages:       # only messages in this room
                for m in user.messages[self]: # extract message
                    msgs.append(m)

        # print in time order
        for m in sorted(msgs, key=lambda x:x.time):
            t = time.ctime(m.time).split()[3] # extract time from timestamp
            print '  ',t,m,
            if m.broadcast:
                print '(BROADCAST)'
            else:
                print
        print

    def display_all_users(self):
        print 'Users in %s: '%(self),
        for user in self.usrs:
            print user,',',
        print
        time.sleep(1)

    def broadcast(self, user, words):
        "User send something too all the other people in this room."
        
        print 'user %s broadcasting to EVERYONE:'%(user)
        for i in self.usrs:
            if i != user:
                # broadcast words should not be new Messages, so say() is not called.
                print "User %s says %s to %s"%(user, words, i)
        time.sleep(1)

    def showAD(self):
        "Show an ad in this room."
        
        print "AD time in '%s':"%(self),
        self.ad.show()
        time.sleep(1)

    def __del__(self):
        self.rooms -= 1

# user_decision = {0:decline, 1:accept} # how to call method in class?

def user_random_decision(user1, user2, rm):
    "user1 decides whether to accpet user2's invitation."
    
    # decision = random.randint(0,1)
    decision = 1
    
    if decision==0:
        user1.decline(rm, user2)
    else:
        user1.accept(rm, user2)
        rm.join(user1)

def test_chatroom():
    p1 = User('Jerry')
    p2 = User('Tom')
    
    rm1 = Room('hello chatroom!')
    rm1.join(p1)    # p1 joined room 'rm1'
    
    rm1.invite(p1, p2)
    user_random_decision(p2, p1, rm1)
    
    p1.say(p2,"Hello "+str(p2),rm1)
    p2.say(p1, "Hi,"+str(p1),rm1)

    p1.show_messages(rm1)
    p1.show_all_messages()
    rm1.display_all_users()
    
    rm1.showAD()

    print
    p3 = User('Violet')
    rm1.invite(p2,p3)
    user_random_decision(p3, p2, rm1)
    
    p2.say(p3, "welcome, "+str(p3), rm1)
    p3.say(p2, "Thanks for inviting me.", rm1)

    p2.show_all_messages()
    rm1.display_all_users()
    
    rm1.showAD()

    print
    rm2 = Room('rm2')
    rm2.join(p3)
    rm2.join(p1)
    p1.say(p3, "It's good to see you here. "+str(p3), rm2)
    rm2.display_all_users()
    rm2.showAD()
    p1.say(p2, "Can I speek to you? " + str(p2), rm2) # test talking to people not in the same room

    print
    p1.say('all', "How are you everyone?", rm1)
    p1.show_all_messages()
    p2.show_all_messages()
    
    print
    rm1.display_all_messages()
    rm2.display_all_messages()
    

if __name__=='__main__':
    test_chatroom()
