import random

class Node:
    '''
        Node of a singly-linked linked list
    '''
    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self):
        # head of the list, None when list is empty
        self.head = None

    def isEmpty(self):
        if not self.head:
            return True
        return False

    def insert(self, x):
        '''
            Inserts a node at the front of the list
            x: Node to be inserted in the list
        '''
        x.next = self.head
        self.head = x

    def delete(self, x):
        '''
            Deletes the first occurence fof given node from the linked list
            Throws exception if node not found
        '''
        curr = self.head
        prev = None
        while curr and x.key != curr.key:
            prev = curr
            curr = curr.next
        if not curr:
            raise Exception("Node not found!")
        prev.next = curr.next
        del(curr)

    def search(self, k):
        '''
            Searches the linked list for the node with key = k
            Returns the node if found, else None
        '''
        curr = self.head
        while curr and curr.key != k:
            curr = curr.next
        return curr

    def print(self):
        curr = self.head
        while curr:
            print (curr.key, end=" ")
            curr = curr.next
        print("\n")


if __name__ == "__main__":
    l = LinkedList()

    for i in range(6):
        key = random.randint(0, 9)
        node = Node(key)
        print ("Inserting {}...".format(key))
        l.insert(node)

    print ("Linked list is: ", end="")
    l.print()

    print ("Result of searching for 5: {}".format(l.search(5)))
    print ("Result of searching for 8: {}".format(l.search(8)))

    print ("Deleting node with key 2...")
    l.delete(Node(2))
    print ("Linked list is: ", end="")
    l.print()
