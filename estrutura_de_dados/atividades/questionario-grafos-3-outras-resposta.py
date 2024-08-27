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