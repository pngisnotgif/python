# 13-9

class queue(list):
    '''
        queue class inherited from list.
    '''

    def __len__(self):
        return super(queue, self).__len__()
    
    def enqueue(self, element):
        self.append(element)

    def dequeue(self):
        l = len(self)

        if l>0:
            element = self[0]
            del self[0]
        else:
            print 'Empty queue.'
            element = []
            
        return element

    def display(self):
        print self


def test_queue():
    q = queue()
    
    q.enqueue('1')
    q.enqueue([2])
    q.enqueue(q)
    q.display()
    
    q.dequeue()
    print q
    
    q.dequeue()
    q.dequeue()
    q.display()
    
    q.dequeue() # test dequeue empty queue
    q.display()
    

if __name__=='__main__':
    test_queue()
