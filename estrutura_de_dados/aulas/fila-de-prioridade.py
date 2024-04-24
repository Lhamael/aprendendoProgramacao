class Node:
  def __init__(self,initdata):
    self.fila = []
    self.file_60 = []
    self.fila_80 = []

  def adiciona_pessoa(self, idade):
    if idade >= 80:
      self.fila_80.append(idade)
    elif idade >= 60:
      self.fila_60.append(idade)
    else:
      self.fila.append(idade)

  def size(self):
    return(len(self.fila) + len(self.file_60) + len(self.fila_80))

  def chama_proximo_fila(self):
    if len(self.fila_80) > 0:
      