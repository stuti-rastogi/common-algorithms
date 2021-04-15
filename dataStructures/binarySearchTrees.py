class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def inorderTraversal(self):
        print ("In-order Traversal\t: ", end="")
        self._inorderTraversalHelper(self.root)
        print ("\n")

    def _inorderTraversalHelper(self, x):
        if x:
            self._inorderTraversalHelper(x.left)
            print (x.key, end=" ")
            self._inorderTraversalHelper(x.right)

    def preorderTraversal(self):
        print ("Pre-order Traversal\t: ", end="")
        self._preorderTraversalHelper(self.root)
        print ("\n")

    def _preorderTraversalHelper(self, x):
        if x:
            print (x.key, end=" ")
            self._preorderTraversalHelper(x.left)
            self._preorderTraversalHelper(x.right)

    def postorderTraversal(self):
        print ("Post-order Traversal\t: ", end="")
        self._postorderTraversalHelper(self.root)
        print ("\n")

    def _postorderTraversalHelper(self, x):
        if x:
            self._postorderTraversalHelper(x.left)
            self._postorderTraversalHelper(x.right)
            print (x.key, end=" ")

    def search(self, k):
        x = self.root
        while (x and x.key != k):
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def maximum(self, x):
        while x.right:
            x = x.right
        return x

    def minimum(self, x):
        while x.left:
            x = x.left
        return x

    def successor(self, x):
        if x.right:
            return self.minimum(x.right)
        else:
            y = x.p
            while y and x != y.left:
                x = y
                y = x.p
            return y

    def predecessor(self, x):
        if x.left:
            return self.maximum(x.left)
        else:
            y = x.p
            while y and x != y.right:
                x = y
                y = x.p
            return y

    def insert(self, z):
        y = None
        x = self.root
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.p = y

        if not y:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def delete(self, z):
        if not z.left:
            self.transplant(z, z.right)
        elif not z.right:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                z.right.p = y
            self.transplant(z, y)
            y.left = z.left
            z.left.p = y

    def transplant(self, u, v):
        if not u.p:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v:
            v.p = u.p


if __name__ == "__main__":
    t = BinarySearchTree()
    print ("Searching for 12\t: {}\n".format(t.search(12)))

    # We will use the below tree to drive the code
    #       12
    #    /      \
    #   5       18
    #  / \     /  \
    # 2   9   15  19
    #           \
    #            17
    t.insert(TreeNode(12))
    t.insert(TreeNode(5))
    t.insert(TreeNode(2))
    t.insert(TreeNode(9))
    t.insert(TreeNode(18))
    t.insert(TreeNode(15))
    t.insert(TreeNode(17))
    t.insert(TreeNode(19))

    t.inorderTraversal()
    t.preorderTraversal()
    t.postorderTraversal()

    print ("Searching for 12\t: {}".format(t.search(12)))
    print ("Searching for 10\t: {}".format(t.search(10)))

    print ()

    print ("Maximum value in tree\t: {}".format(t.maximum(t.root).key))
    print ("Minimum value in tree\t: {}".format(t.minimum(t.root).key))

    print ()

    print ("Successor value of 2\t: {}".format(t.successor(t.search(2)).key))
    print ("Successor value of 12\t: {}".format(t.successor(t.search(12)).key))
    print ("Successor value of 9\t: {}".format(t.successor(t.search(9)).key))

    print ()

    print ("Predecessor value of 15\t: {}".format(t.predecessor(t.search(15)).key))
    print ("Predecessor value of 19\t: {}".format(t.predecessor(t.search(19)).key))
    print ("Predecessor value of 18\t: {}".format(t.predecessor(t.search(18)).key))

    print ()

    print ("Deleting node with no children (2)...")
    t.delete(t.search(2))
    t.preorderTraversal()
    t.postorderTraversal()

    print ("Deleting node with 1 child (5)...")
    t.delete(t.search(5))
    t.preorderTraversal()
    t.postorderTraversal()

    print ("Deleting node with 2 children (12)...")
    t.delete(t.search(12))
    t.preorderTraversal()
    t.postorderTraversal()
