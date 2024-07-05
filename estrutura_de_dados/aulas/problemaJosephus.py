"""
    Adicionar valores
    Criar uma lista circular
    Retirar valor da lista circular
"""

#----------Código menos otimizado---------
from pythonds.basic.queue import Queue

#"""
class Seletor:
    def __init__(self) -> None:
        self.fifo = Queue()
    
    def acrescenta(self, nome):
        self.fifo.enqueue(nome)

    def retira(self):
        return self.fifo.dequeue()

    def rodar(self, qtd):
        while self.fifo.size() > 1:
            for i in range(qtd-1):
                nome = self.retira()
                self.acrescenta(nome)
            self.retira()
        return self.retira()
    

lista = Seletor()
l = ["Josephus", "Timão", "Henrique", "Geronimus", "Cornelius"]
for i in l:
    lista.acrescenta(i)
n = int(input())
print(lista.rodar(n))
#"""
#----------Código mais otimizado---------
#"""
def selecionado(lista,n):
    x = 0
    while len(lista)>1:
        x = (x+n)%len(lista)
        lista.pop(x)
        x = (x-1)%len(lista)
    print(lista[0])

lista = ["Josephus", "Timão", "Henrique", "Geronimus", "Cornelius"]

selecionado(lista, 3)
#"""