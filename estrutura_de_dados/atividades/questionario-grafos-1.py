def converteParaGrafo(lista, tipo):
    grafo = {}
    for aresta in lista:
        if aresta[0] not in grafo:
            grafo[aresta[0]] = {}
        if aresta[1] not in grafo:
            grafo[aresta[1]] = {}

        grafo[aresta[0]][aresta[1]] = aresta[2]
        if tipo == "N":
            grafo[aresta[1]][aresta[0]] = aresta[2]

    return grafo


def criaMatriz(grafo, qtdVertices):
    retorno = ""
    for linha in range(1, qtdVertices + 1):
        retorno = criaElementosMatriz(grafo, qtdVertices, linha, 1)
        print("{}".format(retorno))


def criaElementosMatriz(grafo, qtdVertices, linhaAtual, verticeAtual):
    if qtdVertices < verticeAtual:
        return ""
    if linhaAtual in grafo:
        if verticeAtual in grafo[linhaAtual]:
            peso = f"{grafo[linhaAtual][verticeAtual]}"

            return " " * (4 - len(peso)) + peso + criaElementosMatriz(grafo, qtdVertices, linhaAtual, verticeAtual + 1)

    return "   0" + criaElementosMatriz(grafo, qtdVertices, linhaAtual, verticeAtual + 1)


def Matriz(lista, qtdVertices, qtdArestas, tipoGrafo):
    grafo = converteParaGrafo(lista, tipoGrafo)
    criaMatriz(grafo, qtdVertices)


V, E, C = input().split()
V, E = int(V), int(E)
conexoes = []
for _ in range(E):
    conexoes.append(list(map(int, input().split())))

Matriz(conexoes, V, E, C)