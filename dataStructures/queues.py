# We assign maximum size for our queue and initialize list of that size + 1
# Array of size n holds queue of size n-1 by design
# We use inf for elements that have not been set yet
MAXSIZE = 4

class Queue:
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.queue = [float("inf")] * (MAXSIZE+1)

    def isEmpty(self):
        if self.head ==  self.tail:
            return True
        return False

    def isFull(self):
        if (self.head == self.tail + 1) or \
            (self.tail == MAXSIZE and self.head == 0):
            return True
        return False

    def enqueue(self, x):
        if self.isFull():
            raise Exception("QUEUE OVERFLOW: Queue is full")
        self.queue[self.tail] = x
        if self.tail == MAXSIZE:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("QUEUE UNDERFLOW: Queue is empty")
        x = self.queue[self.head]
        if self.head == MAXSIZE:
            self.head = 0
        else:
            self.head += 1
        return x

    def print(self):
        i = self.head
        while True:
            print (self.queue[i], end=" ")
            i += 1
            if i == MAXSIZE+1:
                i = 0
            if i == self.tail:
                break
        print ("\n")

if __name__ == "__main__":
    q = Queue()
    print ("Enqueue 4...")
    q.enqueue(4)
    print ("Enqueue 1...")
    q.enqueue(1)
    print ("Enqueue 3...")
    q.enqueue(3)
    print ("Queue is: ", end=" ")
    q.print()

    print ("Dequeue...")
    q.dequeue()
    print ("Enqueue 8...")
    q.enqueue(8)
    print ("Enqueue 7...")
    q.enqueue(7)
    print ("Queue is: ", end=" ")
    q.print()

    print ("Dequeue...")
    q.dequeue()
    print ("Dequeue...")
    q.dequeue()
    print ("Queue is: ", end=" ")
    q.print()

    print ("Enqueue 9...")
    q.enqueue(9)
    print ("Dequeue...")
    q.dequeue()
    print ("Queue is: ", end=" ")
    q.print()
