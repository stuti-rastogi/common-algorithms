from stacks import Stack

class QueueUsingStack:
    '''
        Implementing Queue using two stacks
        We implement only enqueue and dequeue methods
    '''
    def __init__(self):
        self.a_stack = Stack(20)
        self.b_stack = Stack(20)

    def enqueue(self, x):
        self.a_stack.push(x)
        print ("Enqueueing element: {}\n".format(x))
        print ("A Stack: ", end="")
        self.a_stack.print()
        print ("B Stack: ", end="")
        self.b_stack.print()
        print ("---------------------------------------------")

    def dequeue(self):
        if not self.b_stack.isEmpty():
            element = self.b_stack.pop()
        else:
            while (self.a_stack.top != 0):
                x = self.a_stack.pop()
                self.b_stack.push(x)
            element = self.a_stack.pop()

        print ("Dequeued element: {}\n".format(element))
        print ("A Stack: ", end="")
        self.a_stack.print()
        print ("B Stack: ", end="")
        self.b_stack.print()
        print ("---------------------------------------------")
        return element


q = QueueUsingStack()
q.enqueue(4)
q.enqueue(1)
q.enqueue(3)
q.dequeue()
q.enqueue(8)
q.dequeue()
