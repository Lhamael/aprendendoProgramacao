# Implementei aqui uma busca por profundidade, contudo ela nao e a mais viavel
"""
def buscaProfundidade(grafo, noAtual, fim, profundidade):
    grafo[noAtual][0] = "G"
    for filho in grafo[noAtual][1:]:
        if filho == fim:
            return profundidade

        if grafo[filho][0] == "W":
            profundidadeEncontrada = buscaProfundidade(grafo, filho, fim, profundidade+1)
            if profundidadeEncontrada != -1:
                return profundidadeEncontrada

    grafo[noAtual][0] = "B"
    return -1
"""
# A opcao mais viavel e utilizar o algoritmo de Dijkstra
## Implemente aqui o algoritmo

def criaGrafo(lista, origem, destino):
    grafo = {}
    for vertice in lista:
        if vertice[0] not in grafo:
            grafo[vertice[0]] = ["W"]
        for aresta in vertice[2:]:

#-------------------------------------------------------------#
            if vertice[0] == origem and aresta == destino or vertice[0] == destino and aresta == origem:
                    return 0
#-------------------------------------------------------------#

            if aresta not in grafo:
                grafo[aresta] = ["W"]

            grafo[vertice[0]].append(aresta)
            grafo[aresta].append(vertice[0])

    return buscaProfundidade(grafo, origem, destino, 0)



n = int(input())
dados = []
alones = []
for i in range(n):
    dados.append(list(map(int, input().split())))
    if dados[i][1] == 0:
        alones.append(dados[i][0])

origem, destino = list(map(int, input().split()))
if origem in alones or destino in alones:
    print("Forevis alonis...")
else:
    qtdContados = criaGrafo(dados, origem, destino)
    if qtdContados == -1:
        print("Forevis alonis...")
    else:
        print(qtdContados)
