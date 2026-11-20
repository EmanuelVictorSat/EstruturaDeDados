from binaryNode import *
class BinaryTree:
    def __init__(self, root=None):
        self._root = root #Asssignment space to an object
    @property
    def root(self):
        return self._root
    @root.setter
    def root(self, newRoot):
        if newRoot != None:
            self._root = newRoot 

    def isEmpty(self):
        if self._root == None:
            return True
        return False

    def search(self, value, node = None):
        if self.root == None or self._root.value == None:
            return False
        if node == None:
            node = self._root
        if node.value == value:
            return True
        if node.isLeaf():
            return False
        if node.left != None:
            if self.search(value, node.left):
                return True
        if node.right != None:
            if self.search(value, node.right):
                return True 
        return False
    