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
        self._size += 1
        return f'New client: {new.password}'

    def service(self):
        if self.isEmpty():
            return 'No clients'
        
        cliente_atendido = self._first
        if self._first == self._last:
            self._first = None
            self._last = None
        else:
            self._first = self._first.next
        self._size -= 1
        return cliente_atendido

    def showClients(self):
        pointer = self._first
        if pointer is None:
            print("Fila vazia")
            return
        while pointer is not None:
            print(f"[{pointer.password}]", end=" ")
            pointer = pointer.next
        print()

    def getNextPassword(self):
        if self.isEmpty():
            return 1
        return self._last.password + 1 

class ServiceDesk: 
    def __init__(self, number = 1):
        self._number = number
        self._client = None
        self._next = None

    @property
    def number(self):
        return self._number
    @property
    def client(self):
        if self._client is None:
            return 0
        return self._client.password
    @property
    def next(self):
        return self._next
    @next.setter
    def next(self, newNext):
        self._next = newNext
    
    def atenderCliente(self, filaDeClientes):
        if filaDeClientes.isEmpty():
            return "No clients"
        clienteEmAtendimento = filaDeClientes.service()
        self._client = clienteEmAtendimento
        return f"Guichê {self._number} atendendo senha: {clienteEmAtendimento.password}"

class ServiceDesks:
    def __init__(self, n):
        self._first = None
        self._n = n
        self._initDesks()
    
    def _initDesks(self):
        for i in range(1, self._n + 1):
            novo_guiche = ServiceDesk(i)
            if self._first is None:
                self._first = novo_guiche
            else:
                pointer = self._first
                while pointer.next is not None:
                    pointer = pointer.next
                pointer.next = novo_guiche

    def getDesk(self, index):
        pointer = self._first
        count = 1
        while pointer is not None:
            if count == index:
                return pointer
            pointer = pointer.next
            count += 1
        return None

    def showQueue(self):
        pointer = self._first
        while pointer is not None:
            print(f"Guichê {pointer.number}: Senha {pointer.client}")
            pointer = pointer.next

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    n = int(input("Digite o número de guichês: "))
    fila_clientes = Clients()
    guiches = ServiceDesks(n)

    while True:
        print("\n--- SITUAÇÃO ATUAL ---")
        print(f"Próxima senha a ser gerada: {fila_clientes.getNextPassword()}")
        print("Fila de espera:", end=" ")
        fila_clientes.showClients()
        print("Situação dos guichês:")
        guiches.showQueue()
        
        print("\nMenu:")
        print("1. Chegada de novo cliente")
        print("2. Atender cliente em um guichê")
        print("0. Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            print(fila_clientes.newClient())
        elif opcao == 2:
            num_guiche = int(input(f"Digite o número do guichê (1 a {n}): "))
            guiche_atual = guiches.getDesk(num_guiche)
            if guiche_atual:
                print(guiche_atual.atenderCliente(fila_clientes))
            else:
                print("Guichê inválido!")
        elif opcao == 0:
            break
        else:
            print("Opção inválida!")