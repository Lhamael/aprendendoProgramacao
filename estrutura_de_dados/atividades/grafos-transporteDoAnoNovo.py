"""
  Lembrar de perguntar o que há de errado com o código
"""
import sys
sys.setrecursionlimit(10**7)

def transporteAnoNovo(qtdCelulas, destino, portais): #portal + celula atual = celula Destino # Ex.: Eu = 1; portal = 2; celula destino = 2 + 1 = 3
  if caminha(1, destino, qtdCelulas, portais):
    print("YES")
  else:
    print("NO")

def caminha(atual, destino, qtdCelulas, portais):
  if atual == destino:
    return True
  if atual >= qtdCelulas:
    return False
  return caminha(atual+portais[atual-1], destino, qtdCelulas, portais)


n, t = input().split()
n=int(n)
t=int(t)
temp = input().split()
a = []
for i in temp:
  a.append(int(i))
transporteAnoNovo(n, t, a)