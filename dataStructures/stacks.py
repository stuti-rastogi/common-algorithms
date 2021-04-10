# We assign maximum size for our stack and initialize list of that size
# We use inf for elements that have not been set yet
MAXSIZE = 10

class Stack:
    def __init__(self):
        self.top = -1
        self.stack = [float('inf')] * MAXSIZE

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def push(self, x):
        if self.top == MAXSIZE-1:
            raise Exception("STACK OVERFLOW: Stack is already full.")
        self.top += 1
        self.stack[self.top] = x

    def pop(self):
        if self.isEmpty():
            raise Exception("STACK UNDERFLOW: Stack is empty")
        self.top -= 1
        return self.stack[self.top + 1]

    def print(self):
        for i in range (self.top+1):
            print (self.stack[i], end=" ")
        print ()


if __name__ == "__main__":
    s = Stack ()
    print ("Pushing 4...")
    s.push(4)
    print ("Pushing 1...")
    s.push(1)
    print ("Pushing 3...")
    s.push(3)
    s.print()

    print ("Popping...")
    s.pop()
    s.print()

    print ("Pushing 8...")
    s.push(8)
    s.print()

    print ("Popping...")
    s.pop()
    print ("Popping...")
    s.pop()
    s.print()

