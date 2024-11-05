"""
  Com dois arrays, tenho que encontrar os valores do array faltando
  arr = [7,2,5,3,5,3]
  brr = [7,2,5,4,6,3,5,3]
  o brr é o array original e está faltando [4,6]
  arr[n]
  brr[m]
  1<=n,m<2*10⁵
  n<=m
  1<=brr[i]<=10⁴
  max(brr) - min(brr) <= 100
"""
def sequencial(lista, item, indice):
  pos = 0
  recorrencia = 0
  while pos < indice:
    if lista[pos] == item:
      recorrencia += 1
    pos += 1

  return recorrencia


def missingNumbers(n, arr, m, brr):
  recorrenciaB = 0
  recorrenciaA = 0
  recorrenciaFaltantes = 0
  faltantes = []
  for i in range(m):
    recorrenciaB = sequencial(brr, brr[i], m)
    recorrenciaA = sequencial(arr, brr[i], n)

    if recorrenciaA != recorrenciaB:
      recorrenciaFaltantes = sequencial(faltantes, brr[i], len(faltantes))
      if recorrenciaFaltantes == 0:
        faltantes.append(brr[i])

    recorrenciaA = 0
    recorrenciaB = 0

  print(faltantes)


n = int(input())
arr = input().split()
arr = [int(i) for i in arr]
m = int(input())
brr = input().split()
brr = [int(i) for i in brr]
valLimitado = True
i = 0

brr.sort()

if n <= m:
  if n >= 1 and m >= 1 and n <= 200000 and m <= 200000:
    while i < m and valLimitado:
      if not(brr[i] >= 1 and brr[i] <= 10000):
        valLimitado = False
      else: 
        i += 1
    if valLimitado:
      if (brr[m-1]-brr[0]) <= 100:
        missingNumbers(n, arr, m, brr)

