# ------------------------ Forma menos otimizada ------------------------------- #

"""dicionario = {}
class ArvoreBinaria:
    def __init__(self, elemento):
        self.raiz = elemento
        self.filhoEsquerda = None
        self.filhoDireita = None
    def insereEsquerda(self, novoNo):
        if self.filhoEsquerda == None:
            self.filhoEsquerda = ArvoreBinaria(novoNo)
        else:
            t = ArvoreBinaria(self.filhoEsquerda.getValorRaiz())
            t.filhoEsquerda = ArvoreBinaria(novoNo)
            self.filhoEsquerda = t

    def insereDireita(self, novoNo):
        if self.filhoDireita == None:
            self.filhoDireita = ArvoreBinaria(novoNo)
        else:
            t = ArvoreBinaria(self.filhoDireita.getValorRaiz())
            t.filhoDireita = ArvoreBinaria(novoNo)
            self.filhoDireita = t

    def getFilhoDireita(self):
        return self.filhoDireita

    def getFilhoEsquerda(self):
        return self.filhoEsquerda

    def setValorRaiz(self, elemento):
        self.raiz = elemento

    def getValorRaiz(self):
        return self.raiz

    def criaArvore(self, numero):
        base = 1
        while numero > base:
            base = self.entraArvore(self)

    def entraArvore(self, arvore):
        if arvore.getFilhoEsquerda():
            arvore.entraArvore(arvore.getFilhoEsquerda())
            return max(arvore.entraArvore(arvore.getFilhoDireita()), arvore.getFilhoDireita().getValorRaiz())


        else:
            arvore.insereEsquerda(arvore.getValorRaiz() * 2)
            arvore.insereDireita((arvore.getValorRaiz() * 2) + 1)

            dicionario[arvore.getValorRaiz() * 2] = arvore.getValorRaiz()
            dicionario[(arvore.getValorRaiz() * 2) + 1] = arvore.getValorRaiz()
            valMax = arvore.getFilhoDireita().getValorRaiz()
            return valMax

    def somaArvoreBinaria(self, numero):
        if not (numero in dicionario):
            return 1
        else:
            return numero + self.somaArvoreBinaria(dicionario[numero])

testes = int(input())
for i in range(testes):
    qtdNos = int(input())
    arvore = ArvoreBinaria(1)
    arvore.criaArvore(qtdNos)
    print(arvore.somaArvoreBinaria(qtdNos))
"""


# ------------------------ Forma mais otimizada ------------------------------- #
def arvoreSacana(n):
    if n == 1:
        return n
    else:
        if n % 2 == 0:
            return arvoreSacana(n // 2) + n
        else:
            return arvoreSacana((n - 1) // 2) + n


testes = int(input())
for i in range(testes):
    n = int(input())
    print(arvoreSacana(n))

