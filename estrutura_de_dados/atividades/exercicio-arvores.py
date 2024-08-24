class Arvore:
    def __init__(self):
        self.raiz = None
        self.esq = None
        self.dir = None

    def insere_raiz(self, raiz):
        self.raiz = raiz
    def insere_esq(self, esquerda):
        self.esq = esquerda

    def insere_dir(self, direita):
        self.dir = direita

    def get_raiz(self):
        return self.raiz

def mostra_arvore(arvore):
    filhos = [arvore.raiz]

    if arvore.esq:
        filhos.append(mostra_arvore(arvore.esq))
    else:
        filhos.append([])
    if arvore.dir:
        filhos.append(mostra_arvore(arvore.dir))
    else:
        filhos.append([])
    return filhos


def altura(ab):
    alt_max = 0
    if ab.esq:
        return max(alt_max, 1+altura(ab.esq))
    if ab.dir:
        return max(alt_max, 1+altura(ab.dir))
    return alt_max

def insere(ab, valor):
    arvore = Arvore()
    arvore.insere_raiz(valor)
    if ab.raiz is None:
        ab.insere_raiz(valor)
    elif ab.esq == None:
        ab.insere_esq(arvore)
    elif ab.dir == None:
        ab.insere_dir(arvore)
    else:
        if altura(ab.esq) > altura(ab.dir):
            insere(ab.dir, valor)
        else:
            insere(ab.esq, valor)

def rotaciona_esquerda(raiz):
    if raiz:
        if raiz.esq != None and raiz.dir != None:
            nova_arvore = raiz.dir
            temporario = nova_arvore.esq
            raiz.insere_dir(temporario)
            nova_arvore.insere_esq(raiz)
            raiz = nova_arvore

            rotaciona_esquerda(raiz.esq)
            rotaciona_esquerda(raiz.dir)
    return raiz


ab = Arvore()
"""
insere(ab, 99)
insere(ab, 93)
insere(ab, 90)
insere(ab, 13)
insere(ab, 21)
insere(ab, 1)
insere(ab, 2)
insere(ab, 3)
print(mostra_arvore(ab))
"""
"""
insere(ab, "a")
insere(ab, "b")
insere(ab, "c")"""
insere(ab, "I")
insere(ab, "H")
insere(ab, "G")
insere(ab, "F")
insere(ab, "E")
insere(ab, "D")
insere(ab, "C")
insere(ab, "B")
insere(ab, "A")
print(mostra_arvore(ab),"\n")
ab = rotaciona_esquerda(ab)
print(mostra_arvore(ab))

#(I(H()())(G(F(E()())(D()()))(C(B()())(A()()))))
#(G(I(H()())(F(E()())(D()())))(C(B()())(A()())))
