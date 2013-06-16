# chatroom: 13-12

class Message(object):
    '''
        message class
    '''

    def __init__(self, msg=None, rec):
        self.msg_str = msg
        if rec == 'all':
            self.broadcast = True
            self.recipient = 'all'
        else:
            self.broadcast = False
            self.recipient = rec
        

    def brdcast(self): pass
        

class User(object):
    '''
        user class
    '''
    
    message = {} # messages of someone in every room.

    def __init__(self, nickname):
        self.name = nickname
        print '%s joined in the chatroom.'%(nickname)
    
    def invite(self, room, person):pass  # invite someone to some room

    def accept(self, room, inviter):pass # accept invitation

    def say(self, listener, words, room=None): pass
        '''
            Say something to someone(listener).

            If room is None, chat in current room.
        '''

        msg = Message(words, listener)
        message.append(msg)

    def show_messages(self, room):
        for msg in message:
            print msg
    
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
   
    def invite(self, inviter, invitee):
        # invite someone to this room
        pass

    def display_all_messages(self):pass

    def display_all_users(self):pass

    def __del__(self):
        self.rooms -= 1

    

def test_chatroom():
    p1 = User('Jerry')
    p2 = User('Tom')

    rm1 = Room('hello chatroom!')
    rm1.invite(p1, p2)
    

if __name__=='__main__':
    test_chatroom()
