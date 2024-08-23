class Arvore:
    def __init__(self) -> None:
        self.raiz = None
        self.filhos = []

    def set_raiz(self, raiz):
        self.raiz = raiz

    def get_raiz(self):
        return self.raiz

    def __str__(self):
        return str(self.imprimeArvore())
    

    def imprimeArvore(self):
        retorno = [self.raiz]
        listaFilhos = []
        for filho in self.filhos:
            listaFilhos.append(filho.imprimeArvore())
        retorno.append(listaFilhos)
        return listaFilhos


    def altura(self):
        alt = 0
        altMax = 0
        for filho in self.filhos:
            altMax = max(altMax, filho.altura()+1)

        return alt+1

    def insereNo(self, valor):
        filho = Arvore()
        filho.set_raiz(valor)
        self.filhos.append(filho)

    def removeNo(self, valor):
        for filho in self.filhos:
            if filho.get_raiz() == valor:
                self.filhos.remove(filho)
                return filho
            else:
                neto = filho.removeNo(valor)
                if neto:
                    return neto
                
        return None

    def getNo(self, valor):
        for filho in self.filhos:
            if filho.get_raiz() == valor:
                return filho
            else:
                neto = filho.getNo(valor)
                if neto:
                    return neto.getNo(valor)

class ArvoreBinaria:
   def __init__(self, obj):
       self.raiz = obj
       self.esq = None
       self.dir = None

    def insereEsq(self, novoNo):
        if self.esq == None:
            self.esq = ArvoreBinaria(novoNo)
        else:
            folha = ArvoreBinaria(novoNo)
            folha.esq = self.esq
            self.esq = folha

    def insereDir(self, novoNo):
        if self.dir == None:
            self.dir = ArvoreBinaria(novoNo)
        else:
            folha = ArvoreBinaria(novoNo)
            folha.dir = self.dir
            self.dir = folha

    def getFilhoDireita(self):
        return self.dir

    def getFilhoEsq(self):
        return self.esq

    def setRaiz(self, obj):
        self.raiz = obj

    def getRaiz(self):
        return self.raiz

            
h = Arvore()

h.set_raiz(33)
h.insereNo(27)
h.insereNo(88)
h.insereNo(51)

no88 = h.getNo(88)
no88.insereNo(23)



print(h)
print("Altura: ", h.altura())


no88 = h.getNo(23)
no88.insereNo(76)

print(h)
print("Altura: ", h.altura())

