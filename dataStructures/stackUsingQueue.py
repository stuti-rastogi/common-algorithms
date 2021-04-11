from queues import Queue

class StackUsingQueue:
    '''
        Implementing Stack using two queues
        We implement only push and pop methods
    '''
    def __init__(self):
        self.a_queue = Queue(20)
        self.b_queue = Queue(20)

    def push(self, x):
        self.a_queue.enqueue(x)
        print ("Pushed element: {}\n".format(x))
        print ("A Queue: ", end = "")
        self.a_queue.print()
        print ("B Queue: ", end = "")
        self.b_queue.print()
        print ("---------------------------------------------")

    def pop(self):
        # dequeue all except one element from A and enqueue to B
        while True:
            x = self.a_queue.dequeue()
            self.b_queue.enqueue(x)
            if (self.a_queue.head + 1 == self.a_queue.tail) or \
                (self.a_queue.head == self.a_queue.MAXSIZE and self.a_queue.tail == 0):
                break

        element = self.a_queue.dequeue()

        # swap queues A and B
        self.a_queue, self.b_queue = self.b_queue, self.a_queue

        print ("Popped element: {}\n".format(element))
        print ("A Queue: ", end = "")
        self.a_queue.print()
        print ("B Queue: ", end = "")
        self.b_queue.print()
        print ("---------------------------------------------")
        return element


s = StackUsingQueue()
s.push(4)
s.push(1)
s.push(3)
s.pop()
s.push(8)
s.pop()
