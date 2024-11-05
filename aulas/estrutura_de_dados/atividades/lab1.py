import lab1ComHashTable

"""
def procuraRepetida(arr):
  repeticoes = 0
  for i in range(len(arr)):
    j = i+1
    verificador = False
    while j < len(arr) and verificador == False:
      if arr[j] == arr[i]:
        repeticoes +=1
        verificador = True
      else:
        j+=1
    i +=1
  return repeticoes
"""
def contador(qtdRoupas, roupas):
  hash = {}
  for i in roupas:
    hash[i] = 0

  for i in roupas:
    if (i in hash) == True:
      hash[i] = hash[i]+1

  repeticoes = 0
  for i in hash:
    repeticoes += (hash[i]-1)

  print(repeticoes)


qtdRoupas = int(input())
roupas = input().split()


"""
  Exemplos:
  5
  A1 A2 A2 A1 B9
  23
  H6 D3 Y7 A1 Z7 M6 Z2 A1 L4 H8 J2 T3 X4 N9 X7 C3 W7 X4 A1 I6 J7 N9 I0
  15
  O2 N7 C8 I3 E5 L5 N5 Q6 U1 G9 T0 A8 Z8 K1 U4
"""