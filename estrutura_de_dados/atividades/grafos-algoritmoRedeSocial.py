"""
  Identificar o que há de errado com o código
"""
n = int(input())
dicionario = {}
repostador = []
postador = []
i = 1

while i <= n:
  y, reposted, x = input().split()
  x=x.lower()
  y=y.lower()
  if x not in dicionario:
    dicionario[x] = []
  dicionario[x].append(y)
  i+=1

print(len(dicionario)+1)