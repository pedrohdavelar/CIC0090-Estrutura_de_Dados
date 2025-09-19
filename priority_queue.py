class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item) #insere no comeco

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop() #remove no final
        else:
            return None
        
    def size(self):
        return len(self.items)

class priorityQueue(Queue):
    def __init__(self):
        self.filaNormal = Queue()
        self.filaPrioritaria = Queue()
        self.filaIdosos = Queue()

    def is_empty(self):
        return self.filaNormal.is_empty() and self.filaPrioritaria.is_empty() and self.filaIdosos.is_empty()
    
    def enqueue(self, item, categoria):
        if categoria == 'N':
            self.filaNormal.enqueue(item)
        elif categoria == 'P':
            self.filaPrioritaria.enqueue(item)
        elif categoria == 'I':
            self.filaIdosos.enqueue(item)

    def dequeue(self):
        if self.filaIdosos.is_empty() == False:
            return self.filaIdosos.dequeue()
        elif self.filaPrioritaria.is_empty() == False:
            return self.filaPrioritaria.dequeue()
        elif self.filaNormal.is_empty() == False:
            return self.filaNormal.dequeue()
        else:
            return None
        
filaPacientes = priorityQueue()

filaPacientes.enqueue("Joao", 'N')
filaPacientes.enqueue("Maria", 'P')
filaPacientes.enqueue("Pedro", 'I')
filaPacientes.enqueue("Ana", 'I')

print(filaPacientes.dequeue())
print(filaPacientes.dequeue())
print(filaPacientes.dequeue())
print(filaPacientes.dequeue())
