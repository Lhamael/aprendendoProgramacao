"""
  A ideia é tentar achar um loop de nós.
  Sugestão: Tente utilizar hashtable com o valor do ponteiro para identificar quando tem mais de um ponteiro apontando para o mesmo lugar.
"""

class No:
  def __init__(self, valInic):
    self.valor = valInic
    self.prox = None

  def getVal(self):
    return self.valor

  def setVal(self, novoValor):
    self.valor = novoValor

  def getProx(self):
    return self.prox

  def setProx(self, novoProx):
    self.prox = novoProx

class criaLista:
  def __init__(self):
    self.cabeca = None
    
  def vazia(self):
    return self.cabeca == None
    
  def novoNo(self, item):
    temp = No(item)
    temp.setProx(self.cabeca)
    self.cabeca = temp

def contaPonteiro(lista):
  dicionario = {}
  while lista.getProx() != None:
    dicionario[]

  