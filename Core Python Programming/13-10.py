# 13-10

# NOT FINISHED

import stack
import queue

class stack_queue(stack, queue):
    l = []

    def __init__(self): # how to init multi-inherited class? 
        super(stack_queue, self).__init__()
    
    def shift(self):
        super(queue, self).dequeue()

    def unshift(self, element):
        l.insert(0,element)

    def push(self):
        super(stack_queue, self).enqueue()

    def pop(self):
        return super(stack_queue, self).pop()

    def display(self):
        for i in l:
            print i,
        print

def test_stk_que():
    sq = stack_queue() # FIXME
    # sq.push(3)
    # sq.display()

if __name__=='__main__':
    test_stk_que()
