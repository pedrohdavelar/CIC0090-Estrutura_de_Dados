import time

def soma_ate(n):
   resultado = 0
   for i in range(1, n + 1):
       resultado = resultado + i
   return resultado

def soma_pa(n):
   return n * (1 + n) / 2


num_testes = 50000
media = 0

for _ in range(num_testes):
    inicio = time.time()
    soma_ate(10000)
    fim = time.time()
    
    tempo_de_execucao = fim - inicio
    media += tempo_de_execucao
    print(f'Tempo: {tempo_de_execucao}')

total = media
media /= num_testes
print(f'Média de tempo: {media}')
print(f'Total de tempo: {total}')