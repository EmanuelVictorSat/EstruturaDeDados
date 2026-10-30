class Client:
    def __init__(self, password: int):
        self._password = password 
        self._next = None

    @property
    def password(self):
        return self._password 
    @property
    def next(self):
        return self._next
    @next.setter
    def next(self, newNext):
        self._next = newNext

class Clients: 
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    @property
    def start(self):
        return self._first
    @property
    def end(self):
        return self._last
    @property
    def size(self):
        return self._size
#MÉTODOS
    def isEmpty(self):
        return self._first == None 

    def newClient(self):
        if self.isEmpty():
            new = Client(1)
            self._first = new
            self._last = new
        else: 
            self._last.next = Client(self._last.password + 1)
            self._last = self._last.next
            new = self._last 
        return f'New client: {new}'

    def service(self):
        if self.isEmpty():
            return 'No clients'
        elif self._first == self._last:
            self._first = None
            self._last = None
            return f'That was the last'
        else:
            self._first = self._first.next
            return f"Client coming"

    def clientsSize(self):
        pointer = self._first
        while pointer is not None:
            self._size += 1
            pointer = pointer.next
        return self._size

    def showClients(self):
        pointer =self._first
        while pointer is not None:
            print(f"Client: {pointer.password}")
            pointer = pointer.next
        return
            
    def showNext(self):
        return self._first

class serviceDesk:
    def __init__(self, number = 1):
        self._number = number
        self._client = None
        self._next = None

    @property
    def number(self):
        return self._number
    @property
    def client(self):
        return self._client
    @property
    def next(self):
        return self._next
    @client.setter
    def client(self, password):
        self._client = password

    def emptyDesk(self):
            return serviceDesk().client == None
    
    def atenderCliente(self, filaDeClientes):
        if filaDeClientes.isEmpty():
            return "No clients"
        clienteEmAtendimento = filaDeClientes.start
        self._client = clienteEmAtendimento
        #Pega o primeiro cliente da fila em guarda em self._client

        filaDeClientes.service()
        #remove o primeiro da fila (ele vai ser atendido e vai embora)
        return f"Guichê: {self._number} atendendo cliente senha: {clienteEmAtendimento.password}"

    def __str__(self):
        return str(self._number)

class serviceDesks:
    def __init__(self):
        self._first = None #lista 
    
    def isEmpty(self):
        return self._first == None

    def newDesk(self):
        if self.isEmpty():
            self._first = serviceDesk(1) 
            return f"First desk: {self._first}"
        else:
            pointer = self._first
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = serviceDesk(pointer.number + 1)

    def showQueue(self):
        pointer = self._first
        while pointer is not None:
            print(pointer.password)
            pointer = pointer.next

