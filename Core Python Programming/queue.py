# 13-9

class queue(object):

    q_list = []

    def enqueue(self, element):
        self.q_list.append(element)

    def dequeue(self):
        l = len(self.q_list)

        if l>0:
            element = self.q_list[0]
            del self.q_list[0]
        else:
            print 'Empty queue.'
            element = None
            
        return element

    def display(self):
        print 'Dump of queue:'
        for i in self.q_list:
            print i,
        print


def test_queue():
    q = queue()
    
    q.enqueue('1')
    q.enqueue([2])
    q.enqueue(q)
    q.display()
    
    q.dequeue()
    q.display()
    q.dequeue()
    q.dequeue()
    q.display()
    
    q.dequeue() # test dequeue empty queue
    q.display()
    

if __name__=='__main__':
    test_queue()
