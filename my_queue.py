import random

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
    
#    def peek(self):
#        if not self.is_empty():
#            return self.items[-1]
#        else:
#            return None
        
    def size(self):
        return len(self.items)
    
def joga_batata_quente(criancas, n):
    q = Queue()
    for crianca in criancas:
        q.enqueue(crianca)
    for _ in range(n):
        #c = q.dequeue()
        #q.enqueue(c)
        q.enqueue(q.dequeue())
    return q.dequeue()



print("Vencedor: ",joga_batata_quente(["Eduardo","Osvaldo","Walter","Judite","Mesmo","Wang"],random.randint(1,6)))

