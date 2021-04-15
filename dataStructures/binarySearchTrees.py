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

    def maximum(self):
        x = self.root
        while x.right:
            x = x.right
        return x

    def minimum(self):
        x = self.root
        while x.left:
            x = x.left
        return x

    def successor(self, x):
        pass

    def predecessor(self, x):
        pass

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
        pass

    def transplant(self, u, v):
        pass


if __name__ == "__main__":
    t = BinarySearchTree()
    print ("Searching for 12\t: {}\n".format(t.search(12)))
    
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

    print ("Searching for 12\t: {}\n".format(t.search(12)))
    print ("Searching for 10\t: {}\n".format(t.search(10)))

    print ("Maximum value in tree\t: {}\n".format(t.maximum().key))
    print ("Minimum value in tree\t: {}\n".format(t.minimum().key))
