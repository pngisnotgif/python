# chatroom: 13-12

import time
import random

class Message(object):
    '''
        message class
    '''

    def __init__(self, rec, msg=None):
        self.msg_str = msg
        if rec == 'all':
            self.broadcast = True
            self.recipient = 'all'
        else:
            self.broadcast = False
            self.recipient = rec

    def __str__(self):
        return self.msg_str

    def show(self):
        return self.__str__()

class User(object):
    '''
        user class
    '''
    
    messages = [] # messages of someone in every room.

    def __init__(self, nickname):
        self.name = nickname
        print '%s joined in the chatroom.'%(nickname)

    def __str__(self):
        return self.name
    
    def invite(self, room, person):  # invite someone to some room
        print "{} sent invitation to {} for joining '{}'".format(self, person, room)

    def accept(self, room, inviter): # accept invitation
        print "{} accepted invitation from {} to join '{}'"\
              .format(self, inviter, room)

    def decline(self, room, inviter):
        print "{} declined invitation from {} to join '{}'"\
              .format(self, inviter, room)

    def say(self, listener, words, room=None): 
        '''
            Say something to someone(listener).

            If room is None, chat in current room.
        '''

        msg = Message(words, listener)
        self.messages.append(msg)
        print "{} says '{}' to {}.".format(self, words, listener)
        print 'type of msg: %r'%(type(msg))
        print 'msg=%s'%msg.show()

    def show_messages(self, room):
        for msg in self.messages:
            print msg.show()
    
    def show_all_messages(self):pass


class Ad(object):
    '''
        Advertisement class
    '''

    def __init__(self):
        self.ad = 'This is an ad.'

    def show(self):
        print self.ad
        

class Room(object):

    rooms = 0

    def __init__(self, rm_name = None):
        'create a room with a name.'
        
        self.rooms += 1
        
        if not rm_name is None:
            self.name = rm_name
        else:
            self.name = 'rm' + str(self.rooms)

        self.perm = {}

        print 'Room "%s" is created.'%(rm_name)

    def __str__(self):
        return 'Room %s'%(self.name)
   
    def invite(self, inviter, invitee):
        # invite someone to this room
        inviter.invite(self.name, invitee)

    def add_permission(self, inviter, invitee):
        'record accepted permission'
        self.perm[inviter] = invitee
        self.perm[invitee] = inviter

    def get_permission(self, user1, user2):
        if user1 in self.perm.keys() or user2 in self.perm.keys():
            return True
        else:
            return False

    def display_all_messages(self):pass

    def display_all_users(self):pass

    def broadcast(self, user): pass

    def __del__(self):
        self.rooms -= 1

# user_decision = {0:decline, 1:accept} # how to call method in class?

def user_random_decision(user1, user2, rm):
    # decision = random.randint(0,1)
    decision = 1
    if decision==0:
        user1.decline(rm, user2)
    else:
        user1.accept(rm, user2)
        rm.add_permission(user1, user2)

def test_chatroom():
    p1 = User('Jerry')
    p2 = User('Tom')

    time.sleep(1)
    
    rm1 = Room('hello chatroom!')

    time.sleep(1)
    rm1.invite(p1, p2)
    user_random_decision(p1, p2, rm1)
    if rm1.get_permission(p1, p2):
        p1.say(p2,"Hello "+str(p2))
        time.sleep(1)
        p2.say(p1, "Hi,"+str(p1))
        time.sleep(1)

        p1.show_messages(rm1)
        p2.show_messages(rm1)

 
    
    

if __name__=='__main__':
    test_chatroom()
