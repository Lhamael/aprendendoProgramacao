from pythonds.basic.stack import Stack

class FilaComDuasPilhas():
    def __init__(self) -> None:
        self.pilha1 = Stack()
        self.pilha2 = Stack()

    def enqueue(self, elemento):
        self.pilha1.push(elemento)

    def dequeue(self):
        return self.pilha2.pop()
    
    def move(self, pilha_Origem, pilha_Destino, string):
        quantidade = pilha_Origem.size()
        for i in range(pilha_Origem.size()):
            pilha_Destino.push(pilha_Origem.pop())
        print("MOVE "+string+" "+str(quantidade))

    def drop(self, quantidade):
        if self.pilha1.size()<quantidade:
            self.move(self.pilha2, self.pilha1, "2->1")
        for i in range(quantidade):
            self.enqueue(i)
        print("DROP 1 "+str(quantidade))

    def take(self, quantidade):
        if self.pilha2.size() < quantidade:
            self.move(self.pilha1, self.pilha2, "1->2")
        for i in range(quantidade):
                self.dequeue()
        print("TAKE 2 "+str(quantidade))

while True:
    operacoes = int(input())
    if operacoes == 0:
        break
    fila = FilaComDuasPilhas()
    for i in range(operacoes):
        operacao = input()
        comando,quantidade = operacao.split(" ")
        if comando == "DROP":
            fila.drop(int(quantidade))
        elif comando == "TAKE":
            fila.take(int(quantidade))