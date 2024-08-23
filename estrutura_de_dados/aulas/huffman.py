class No:
  def __init__(self, caracter, frequencia) -> None:
    self.caracter = caracter
    self.frequencia = frequencia
    self.esquerda = None
    self.direita = None

def huffmann_calcula_frequencia(texto):
  lista_frequencia = {}
  for letra in texto:
    try:
      lista_frequencia[letra] += 1
    except:
      lista_frequencia[letra] = 1

  return lista_frequencia

def huffmann_constroi_arvore(lista_frequencia):
  lista_nos = []
  for letra,frequencia in lista_frequencia.item():
    novo_no = No(letra, frequencia)
    acrescenta_lista(lista_nos, novo_no)

  while len(lista_nos) > 1:
    filho_esquerda = lista_nos.pop(0)
    filho_direita = lista_nos.pop(0)
    pai = No(None, filho_direita.frequencia+filho_esquerda.frequencia)
    pai.esquerda = filho_esquerda
    pai.direita = filho_direita
    acrescenta_lista(lista_nos, pai)

  return lista_nos[0]


def acrescenta_lista(lista_nos, no):
  if len(lista_nos) == 0:
    lista_nos.append(no)
  else:
    for indice in range(len(lista_nos)):
      if lista_nos[indice].frequencia >= no.frequencia:
        break
    lista_nos.insert(indice, no)

def huffmann_constroi_tabela_conversao(raiz):
  tabela_codificadora = {}

  def huffman_codificador(prefixo, no_atual):
    if no_atual.letra is not None:
      tabela_codificadora[no_atual.letra] = prefixo
    else:
      huffman_codificador(prefixo+"0", no_atual.esquerda)
      huffman_codificador(prefixo+"1", no_atual.direita)

  huffman_codificador("", raiz)
  return tabela_codificadora

def algoritmo_codificador_de_huffmann(texto):

  lista_frequencia = huffmann_calcula_frequencia(texto)
  arvore_frequencia = huffmann_constroi_arvore(lista_frequencia)
  tabela_codificada = huffmann_constroi_tabela_conversao(arvore_frequencia)

  texto_codificado = ''
  for caracter in texto:
    texto_codificado += tabela_codificada[caracter]

  return texto_codificado

def algoritmo_decodificador_de_huffmann(texto_codificado, arvore_de_frequencia):

  texto_decodificado = ''
  no_atual = arvore_de_frequencia

  for bit in texto_codificado:
    if bit == '0':
      no_atual = no_atual.esquerda
    else:
      no_atual = no_atual.direita

    if no_atual.caracter is not None:
      texto_decodificado += no_atual.caracter
      no_atual = arvore_de_frequencia

  return texto_codificado

# Exemplo
texto = "abracadabra!"


texto_codificado = algoritmo_codificador_de_huffmann(texto)
print(f"Texto codificado: {texto_codificado}")

arvore_de_Huffmann = huffmann_constroi_arvore(huffmann_calcula_frequencia(texto))
texto_decodificado = algoritmo_decodificador_de_huffmann(texto_codificado, arvore_de_Huffmann)
print(f"Texto original: {texto_decodificado}")