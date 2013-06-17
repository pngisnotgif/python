# 13-8

class stack(list):
    '''
        stack class inherited from list
    '''
    
    def push(self, element):
        if element:
            self.append(element)

    def pop(self):
        if 'pop' in dir(stack.__base__):
            print 'Using builtin pop()'
            try:
                element = super(stack,self).pop()   # must use super, otherwise looping forever here.
            except IndexError:
                element = []
                
            return element
        else:
            print 'Using my pop()'
            l = len(self)
            if l>0:
                element = self[l-1]
                del self[l-1]
                return element
            else:
                return []

    def __len__(self):
        return super(stack, self).__len__()
    
    def isempty(self):
        return len(self)==0

    def peek(self):
        'get item of top of stack, without deleting it.'
        
        l = len(self)
        if l>0:
            element = self[l-1]
            return element
        else:
            return []

    def display(self):
        print self

def test_stack():
    s = stack()
    s.push(1)
    s.display()

    s.push(['2'])
    s.display()
    print 'length of s:',len(s)

    print 'using slice s[:]:', s[:] # need slice operator

    s.pop()
    s.display()

    print 'Top item of stack:',s.peek()
    print s # equals to s.display()

    print s.isempty()

    s.pop()
    s.display()
    print s.isempty()

    s.pop()
    print s.peek()
    
    
if __name__=='__main__':
    test_stack()
