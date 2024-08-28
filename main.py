"""#print("Hello, World!")
class AB:
  def __init__(self) -> None:
    self.raiz = None
    self.esq = None
    self.dir = None

  def insere_raiz(self, valor):
    self.raiz = valor

  def insere_esq(self, valor):
    t = AB()
    t.insere_raiz(valor)
    self.esq = t

  def insere_dir(self, valor):
    t = AB()
    t.insere_raiz(valor)
    self.dir = t

  def get_raiz(self):
    return self.raiz

  def get_esq(self):
    return self.esq

  def get_dir(self):
    return self.dir

def insereValor(arvore, valor):
  if arvore:
    if arvore.get_raiz() == None:
      return arvore.insere_raiz(valor)
    else:
      if valor > arvore.get_raiz():
        return insereValor(arvore.get_dir(), valor)
      else:
        return insereValor(arvore.get_esq(), valor)
  else:
    arvore = AB()
    arvore.insere_raiz(valor)
    return

def converteStr(arvore, acao):
  conjunto = []
  def preorder(arvore):
    if arvore:
      conjunto.append(arvore.get_raiz())
      preorder(arvore.get_esq())
      preorder(arvore.get_dir())
      
  def inorder(arvore):
    if arvore:
      preorder(arvore.get_esq())
      conjunto.append(arvore.get_raiz())
      preorder(arvore.get_dir())
  
  def posorder(arvore):
    if arvore:
      preorder(arvore.get_esq())
      preorder(arvore.get_dir())
      conjunto.append(arvore.get_raiz())

  if acao == "in":
    inorder(arvore)
  if acao == "pre":
    preorder(arvore)
  if acao == "pos":
    posorder(arvore)

  palavra = str(conjunto[0])
  for i in conjunto[1:]:
    palavra += f" {i}"
  print(palavra)
  
  
arvore = AB()
while True:
  valor = input()
  if valor != "quack":
    if valor == "in":
      converteStr(arvore, "in")
    elif valor == "pre":
      converteStr(arvore, "pre")
    elif valor == "pos":
      converteStr(arvore, "pos")
    else:
      insereValor(arvore, int(valor))
  else:
    break
  """

vertices, arestas = [], []
n = int(input())
for _ in range(n):
  id, A, *vizinhos = input().split()
  vertices.append(int(id))
  for i in range(0, len(vizinhos), 2):
    arestas.append((vertices[-1], int(vizinhos[i+1]), int(vizinhos[i])))

total = 0
arestas.sort(reverse=True) #Ordenar de forma descrescente
dicionario = {id: set() for id in vertices}

while arestas:
  origem, destino, tempo = arestas.pop()

  if destino not in dicionario[origem]:
    dicionario[origem].add(destino)
    dicionario[destino].add(origem)
    dicionario[origem] |= dicionario[destino]
    dicionario[destino] |= dicionario[origem]

    for id in dicionario[origem]:
      dicionario[id] |= dicionario[origem]

    total += tempo

print(f'R$ {total * 3.14:.2f}')