class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

def verifica_duplicata(expressao):

    pilha = Stack()
    placeholders = {'(': 'p_x', '[': 'b_x', '{': 'c_x'}

    for char in expressao:
        if char in ')]}':
            if pilha.isEmpty():
                continue

            opening_char = ''
            if char == ')': opening_char = '('
            elif char == ']': opening_char = '['
            else: opening_char = '{'
            
            expected_placeholder = placeholders.get(opening_char)

            content = []
            # Desempilha o conteúdo do bloco
            while not pilha.isEmpty() and pilha.peek() != opening_char:
                content.append(pilha.pop())
            
            if pilha.isEmpty():
                continue
            
            pilha.pop()

            # --- VERIFICAÇÃO DAS CONDIÇÕES DE DUPLICATA ---
            # 1. Conteúdo vazio, ex: ()
            if len(content) == 0:
                return True
            
            # 2. Conteúdo é um único placeholder do mesmo tipo, ex: ((...))
            if len(content) == 1 and content[0] == expected_placeholder:
                return True

            # Se não for duplicata, empilha um placeholder para o bloco resolvido
            pilha.push(expected_placeholder)

        else: # Se não for um fechamento, apenas empilha
            pilha.push(char)

    return False


N = int(input())

for _ in range(N):
    expressao = input()
    if verifica_duplicata(expressao):
        print("A expressão possui duplicata.")
    else:
        print("A expressão não possui duplicata.")
