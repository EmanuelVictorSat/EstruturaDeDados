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

    def searchFor(self, value):
        p = self._root
        def scan(node):
            if node is None:
                return False
            if node.value == value:
                return True
            return scan(node.left) or scan(node.right)
        return scan(p)
    

    def percorreEmOrdem(self):
        result = []
        def run(node):
            if node is not None:
                run(node.left)
                result.append(node.value)
                run(node.right)
        run(self._root)
        return result

    def percorrePreOrdem(self):
        result = []
        def run(node):
            if node is not None:
                result.append(node.value)
                run(node.left)
                run(node.right)
        run(self._root)
        return result

    def percorrePosOrdem(self):
        result = []
        def scanTree(node):
            if node is not None:
                scanTree(node.left)
                scanTree(node.right)
                result.append(node.value)
        scanTree(self._root)
        return result
    def countNodes(self):
        def scan(node):
            if node is None:
                return 0
            return 1 + scan(node.left) + scan(node.right)
        return scan(self._root)
    def countLeafs(self, node = None):
        if node is None:
            node = self._root
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.countLeafs(node.left) + self.countLeafs(node.right) 



     























arvore = BinaryTree()
no = Node(10)
no.left = Node(15)
no.right = Node(20)
no.left.left = Node(102)
no.right.right = Node(210)
no.right.left = Node(7)
no.left.right = Node(233)
arvore.root = no
print(arvore.percorreEmOrdem())
print(arvore.percorrePosOrdem())
print(arvore.percorrePreOrdem())
print(arvore.countNodes())
print(arvore.countLeafs())
print(arvore.searchFor(210))