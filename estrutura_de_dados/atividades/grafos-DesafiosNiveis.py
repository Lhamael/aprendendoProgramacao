import sys
sys.setrecursionlimit(10**9+7)

def qtdPercursos(destino, nivelAtual, conexoes, qtdPercursosPossiveis):
  if nivelAtual == destino:
    return qtdPercursosPossiveis+1
  for portais in conexoes[nivelAtual]:
    qtdPercursosPossiveis = qtdPercursos(destino, portais, conexoes, qtdPercursosPossiveis)

  return qtdPercursosPossiveis

n, m = input().split()
n = int(n)
m = int(m)
portaisNiveis = {}
for i in range(m):
  a, b = input().split()
  a = int(a)
  b = int(b)
  if a not in portaisNiveis:
    portaisNiveis[a] = []
  portaisNiveis[a].append(b)
"""
for niveis, portais in portaisNiveis.items():
  print(f"O nivel {niveis} tem os portais para {portais}")
"""
print(qtdPercursos(n, 1, portaisNiveis, 0))