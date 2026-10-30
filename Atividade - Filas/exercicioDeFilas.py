class No:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data
    @property
    def next(self):
        return self._next
    @data.setter #Method setter for the data property
    def data(self, newData):
        self._data = newData
    @next.setter
    def next(self, newObj):
        self._next = newObj

class Queue: #Queue
    def __init__(self):
        self._start = None
        self._end = None

    @property
    def start(self):
        return self._start
    @property
    def end(self):
        return self._end

    def empty(self):
        return self._start == None
    
    def insert(self, newOb):
        if self._start == None: #is empty
            self._start = newOb
            self._end = newOb
        else:
            self._end.next = newOb #There's some object
            self._end = newOb

    def remove(self):
        if self.empty():
            self._start = None
            self._end = None
            return "Empty queue"
        else:
            removed = self._start
            self._start = self._start.next #Lá se foi!
            return removed

    def showFirst(self):
        return self._start
    
    def showQueue(self):
        element = self._start
        if self.empty():
            return "File is empty"
        while element is not None:
            print(element.data)
            element = element.next
        return "That is your queue"

    def queueSize(self):
        element = self._start
        size = 1 #He will not count the last
        if self.empty():
            return "File is empty"
        while element.next is not None:
            size += 1
            element = element.next
        return size

    def clean(self):
        self._start = None

queue = Queue()
option = int(input(
    "Select an option:\n" 
    "1 - Insert\n"
    "2 - Remove\n" 
    "3 - Show First Element\n"
    "4 - Show Queue\n"
    "5 - Show Size\n"
    "6 - Clean the queue\n" 
    "0 - Job is done\n"
))

while option != 0:
    if option == 1:
        newOb = No(input("Data: "))
        queue.insert(newOb)
    elif option == 2:
        queue.remove()
    elif option == 3:
        queue.showFirst()
    elif option == 4:
        queue.showQueue()
    elif option == 5:
        print(queue.queueSize())
    elif option == 6:
        queue.clean()

    option = int(input(
        "Select an option:\n" 
        "1 - Insert\n"
        "2 - Remove\n" 
        "3 - Show First Element\n"
        "4 - Show Queue\n"
        "5 - Show Size\n"
        "6 - Clean the queue\n" 
        "0 - Job is done\n"
    ))
    