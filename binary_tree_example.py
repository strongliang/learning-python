from collections import deque
class EmptyTree(object):
    """Represents an empty tree."""
    # Supported methods
    def isEmpty(self):
        return True
    def __str__(self):
        return ""
    def __iter__(self):
        """Iterator for the tree."""
        return iter([])
    def preorder(self, lyst):
        return
    def inorder(self, lyst):
        return
    def postorder(self, lyst):
        return

class BinaryTree(object):
    """Represents a nonempty binary tree."""
    # Singleton for all empty tree objects
    THE_EMPTY_TREE = EmptyTree()
    def __init__(self, item):
        """Creates a tree with
        the given item at the root."""
        self._root = item
        self._left = BinaryTree.THE_EMPTY_TREE
        self._right = BinaryTree.THE_EMPTY_TREE
    def isEmpty(self):
        return False
    def getRoot(self):
        return self._root
    def getLeft(self):
        return self._left
    def getRight(self):
        return self._right
    def setRoot(self, item):
        self._root = item
    def setLeft(self, tree):
        self._left = tree
    def setRight(self, tree):
        self._right = tree
    def removeLeft(self):
        left = self._left
        self._left = BinaryTree.THE_EMPTY_TREE
        return left
    def removeRight(self):
        right = self._right
        self._right = BinaryTree.THE_EMPTY_TREE
        return right
    def __str__(self):
        """Returns a string representation of the tree
        rotated 90 degrees to the left."""
        def strHelper(tree, level):
            result = ""
            if not tree.isEmpty():
                result += strHelper(tree.getRight(), level + 1)
                result += "   " * level
                result += str(tree.getRoot()) + "\n"
                result += strHelper(tree.getLeft(), level + 1)
            return result
        return strHelper(self, 0)
    def __iter__(self):
        """Iterator for the tree."""
        lyst = []
        self.inorder(lyst)
        return iter(lyst)
    def preorder(self, lyst):
        """Adds items to lyst during
        a preorder traversal."""
        lyst.append(self.getRoot())
        self.getLeft().preorder(lyst)
        self.getRight().preorder(lyst)
    def inorder(self, lyst):
        """Adds items to lyst during
        an inorder traversal."""
        self.getLeft().inorder(lyst)
        lyst.append(self.getRoot())
        self.getRight().inorder(lyst)
    def postorder(self, lyst):
        """Adds items to lystduring
        a postorder traversal."""
        self.getLeft().postorder(lyst)
        self.getRight().postorder(lyst)
        lyst.append(self.getRoot())
    def levelorder(self, lyst):
        """Adds items to lyst during
        a levelorder traversal."""
        # levelsQueue = LinkedQueue()
        levelsQueue = deque ([])
        levelsQueue.append(self)
        while levelsQueue != deque():
            node = levelsQueue.popleft()
            lyst.append(node.getRoot())
            left = node.getLeft()
            right = node.getRight()
            if not left.isEmpty():
                levelsQueue.append(left)
            if not right.isEmpty():
                levelsQueue.append(right)
                
                
#from binarytree import BinaryTree
lst = ["5", "+", "2"]
for i in range(len(lst)):
    b = BinaryTree(lst[0])
    d = BinaryTree(lst[1])
    f = BinaryTree(lst[2])
# Build the tree from the bottom up, where
# d is the root node of the entire tree
d.setLeft(b)
d.setRight(f)
def size(tree):
    if tree.isEmpty():
        return 0
    else:
        return 1 + size(tree.getLeft()) + size(tree.getRight())
def frontier(tree):
    """Returns a list containing the leaf nodes
    of tree."""
    if tree.isEmpty():
        return []
    elif tree.getLeft().isEmpty() and tree.getRight().isEmpty():
        return [tree.getRoot()]
    else:
        return frontier(tree.getLeft()) + frontier(tree.getRight())
print ("Size:", size(d))
print ("String:")
print (d)