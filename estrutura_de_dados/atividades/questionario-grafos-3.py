def lista_adjacencia(dadosVizinhanca):
  vizinhos_adj = {}
  for vizinhos in dadosVizinhanca:
    if vizinhos[0] not in vizinhos_adj:
      vizinhos_adj[vizinhos[0]] = {}
    for i in range(2, len(vizinhos[2:])+1, 2):
      if vizinhos[i+1] not in vizinhos_adj:
        vizinhos_adj[vizinhos[i+1]] = {}
      vizinhos_adj[vizinhos[0]][vizinhos[i+1]] = vizinhos[i]
      vizinhos_adj[vizinhos[i+1]][vizinhos[0]] = vizinhos[i]
  return vizinhos_adj

def algoritmo_de_Dijkstra(vizinhos_adj, inicio):
  distancia = {no:[float('inf'), 1] for no in vizinhos_adj}
  distancia[inicio][0] = 0

  lista_prioridade = [(0, inicio)]

  while len(lista_prioridade) != 0:
    distancia_atual, no_atual = lista_prioridade.pop(0)

    if distancia_atual > distancia[no_atual][0]:
      continue

    for vizinho, peso in vizinhos_adj[no_atual].items():
      distancia_total = distancia_atual + peso

      if distancia_total < distancia[vizinho][0]:
        distancia[vizinho][0] = distancia_total
        distancia[vizinho][1] = no_atual
        lista_prioridade.append((distancia_total, vizinho))

  return distancia

"""
def distancia_verdadeira(distancias, residencia):
  if distancias[residencia][1] == 1:
    return distancias[residencia][0]
  return distancias[residencia][0] - distancia_verdadeira(distancias, distancias[residencia][1])
"""

def sistemaTubulucacao(dadosVizinhanca):
  vizinhos_adj = lista_adjacencia(dadosVizinhanca)
  inicio = 1
  distancias = algoritmo_de_Dijkstra(vizinhos_adj, inicio)
  soma = 0
  for residencia in distancias:
    if distancias[residencia][1] == 1:
      soma += distancias[residencia][0]
    else:
      temp = distancias[residencia][1]
      soma += distancias[residencia][0] - distancias[temp][0]
  print(f"R$ {soma*3.14:.2f}")





n = int(input())
j = n
dados = []
for _ in range(n):
  dados.append(list(map(int, input().split())))
sistemaTubulucacao(dados)