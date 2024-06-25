# Aqui veremos alguns algoritmos de busca

# Busca sequencial
def buscaSequencial(lista, item):
  proximo = 0
  encontrouItem = False
  while proximo < len(lista) and not encontrouItem:
    if lista[proximo] == item:
      encontrouItem = True
    else:
      proximo = proximo + 1
  return encontrouItem

# Busca Binária não recursiva
def Binaria(lista, item):
  primeiro = 0
  ultimo = len(lista) - 1
  encontrouItem = False
  while primeiro <= ultimo and not encontrouItem:
    pontoMedio = (primeiro + ultimo) // 2
    if lista[pontoMedio] == item:
      encontrouItem = True
    elif item < lista[pontoMedio]:
      ultimo = pontoMedio - 1
    else:
      primeiro = pontoMedio + 1
  return encontrouItem

# Busca Binária recursiva
def binariaRecursiva(lista, item):
  
  if len(lista) == 0:
    return False
  else:
    pontoMedio = len(lista) // 2
    if lista[pontoMedio] == item:
      return True
    elif item < lista[pontoMedio]:
      return binariaRecursiva(lista[:pontoMedio], item)
    else:
      return binariaRecursiva(lista[pontoMedio+1:], item)

# Hash Table
# Neste caso vou dar um exemplo pra ficar mais facil
def contador(qtdRoupas, listaRoupas):
  hash = {} # Isso é um Hash Table
  for i in listaRoupas:
    hash[i] = 0 # Aqui, estamos transformando os elementos da lista em indices da hash

  # Neste caso, ele vai verificar se na lista existem repetições, se houver alguma repetição ele aumenta em 1 o valor na posição especificada.
  for i in listaRoupas:
    if (i in hash) == True:
      hash[i] = hash[i]+1

  # Por fim, aqui ele verifica quantias repetições existem.
  # Neste caso, ele vai passando hash por hash e vai somando a quantidade de elementos que existem na hash subtraido de 1 para não haver duplicação.
  repeticoes = 0
  for i in hash:
    repeticoes += (hash[i]-1)

  print(repeticoes)