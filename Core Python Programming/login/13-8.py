# 13-8

class stack(object):

    stacks = []
    
    def push(self, element):
        if element:
            self.stacks.append(element)

    def pop(self):
        if 'pop' in dir(self.stacks):
            print 'Using builtin pop()'
            try:
                element = self.stacks.pop()
            except IndexError:
                element = None
                
            return element
        else:
            print 'Using my pop()'
            l = len(self.stacks)
            if l>0:
                element = self.stacks[l-1]
                del self.stacks[l-1]
                return element
            else:
                return None

    def isempty(self):
        return len(self.stacks)==0

    def peek(self):
        'get item of top of stack, without deleting it.'
        
        l = len(self.stacks)
        if l>0:
            element = self.stacks[l-1]
            return element
        else:
            return None

    def display(self):
        print 'Stack:'
        for i in self.stacks:
            print i,
        print

def test_stack():
    s = stack()
    s.push(1)
    s.display()

    s.push(['2'])
    s.display()

    # print s[:] # need slice operator

    s.pop()
    s.display()

    print 'Top item of stack:',s.peek()
    s.display()

    print s.isempty()

    s.pop()
    s.display()
    print s.isempty()

    s.pop()
    print s.peek()
    

    
if __name__=='__main__':
    test_stack()
