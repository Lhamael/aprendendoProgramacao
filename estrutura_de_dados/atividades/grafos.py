class ExercicioGrafo:

  def todosOsCaminhosParaOAlvo(self, graph: list[list[int]]):
    caminhos = []
    def procuraAlvo(graph, verticeAtual, verticeFinal, caminhoAtual):

      caminhoAtual = caminhoAtual.copy()
      caminhoAtual.append(verticeAtual)

      if verticeAtual == verticeFinal:
        caminhos.append(caminhoAtual)
        return
      else:
        adjacentes = graph[verticeAtual]
        for adjacente in adjacentes:
          procuraAlvo(graph, adjacente, verticeFinal, caminhoAtual)



    procuraAlvo(graph, 0, len(graph)-1, [])
    return caminhos

#grafo = [[1,2],[3],[3],[]] 
#grafo =  [[4,3,1],[3,2,4],[3],[4],[]]
grafo = [[1,7],[2,3,4],[4,5],[5],[6,7],[],[]]

exercicioGrafo = ExercicioGrafo()

print(exercicioGrafo.todosOsCaminhosParaOAlvo(grafo))