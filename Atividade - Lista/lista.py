from no import Node
class Lista:
    def __init__(self):
        self._first = None
        self._size= 0
    @property
    def head(self):
        return self._first
    @head.setter
    def head(self, newHead):
        self._first = newHead
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, newSize):
        self._size = newSize
#METHODS
    def isEmpty(self):
        return self._first == None
    def getSize(self):
        return self._size
    def getValue(self, position):
        pointer = self._first
        element = 1
        while element != position:
            pointer = pointer.next
            element += 1
        return pointer.data
    def getPosition(self, valorDoNo):
        pointer = self._first
        position = 1
        while pointer is not None:
            position += 1
            if pointer.data == valorDoNo:
                return f"Position: {position}"
            else:
                pointer = pointer.next
        return "Não encontrado"
    def insertOnFirstPosition(self, newObj):
        if self.isEmpty():
            self._first = newObj
        newObj.next = self._first
        self._first = newObj
    def insertOnLastPosition(self, newObj):
        if self.isEmpty():
            self._first = newObj
        else:
            pointer = self._first
            while pointer is not None:
                pointer = pointer.next
            pointer.next = newObj
        return f"{newObj} on the last position!"
    def insertOnDefinedPosition(self, objectValue, position):
        p = self._first
        h = self._first.next
        findPosition = 1
        if self.isEmpty(): 
            return self.insertOnFirstPosition(Node(objectValue))
        elif position == 1: 
            return self.insertOnFirstPosition(Node(objectValue))
        elif position > self.getSize(): 
            return self.insertOnLastPosition(Node(objectValue))
        elif h == None: 
            p.next = Node(objectValue)
        else:
            while findPosition != position - 1:
                p = p.next
                h = h.next
                findPosition += 1
            p.next = Node(objectValue)
            p.next.next = h
    def insertOnAscendingOrder(self, value):
    newElement = Node(value)
    p = self._first
    # Lista vazia
    if self._first is None:
        self._first = newElement
        return f"{newElement.value} adicionado"
    # Insere no início
    if p.value >= value:
        newElement.next = p
        self._first = newElement
        return f"{newElement.value} adicionado"
    q = self._first.next
    while q is not None:
        if q.value >= value:
            p.next = newElement
            newElement.next = q
            return f"{newElement.value} adicionado"
        p = q
        q = q.next
    # Insere no final
    p.next = newElement
    return f"{newElement.value} adicionado"
    def removeFirst(self):
        if self.isEmpty():
            return f"Lista Vazia"
        elif self.getSize() == 1:
            self._first = None
        else:
            self._first = self._first.next
    def removeLast(self):
        p = self._first
        if self.isEmpty():
            return "Lista Vazia"
        elif self.getSize() == 1:
            self._first = None
        while p.next is not None:
            p.next = None
    def removeByPosition(self, position):
        p = self._first
        h = p.next
        find = 1
        if self.isEmpty():
            return "Lista vazia"
        elif self.getSize() == 1:
            self._first = None
        elif position == 1:
            self._first = self._first.next
        elif position < 1 or position > self.getSize():
            raise IndexError(f"Erro: Índex {position} fora dos limites da fila")
        else:
            while find != position - 1:
                p = p.next
                h = h.next
                find += 1
            p.next = h.next
    def removeByValue(self, value):
        if self.isEmpty():
            return "Lista vazia"
        if self._first.data == value:
            self._first = self._first.next
            return
        f = self._first
        s = f.next
        while s is not None:
            if s.data == value:
                f.next = s.next
                return
            f = f.next
            s = s.next
        return "Not found"
    def clean(self):
        self._first = None
    def showList(self):
        p = self._head
        while p is not None:
            print(p.data)
            p = p.next
    def search(self, valueOfSearch):
        search = self._first
        while search is not None:
            if search.value == valueOfSearch:
                print("Valor encontrado!")
                return True
            else:
                search = search.next
    