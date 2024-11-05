"""
Casa = S e T
Arvores = A(Macieira) e B(Laranjeira)
Qtd de Maçãs e Laranjas: M(Maçãs) e N(Laranjas)
Apples
Oranges
"""
def countApplesAndOranges(s,t,a,b,n,m,apples,oranges):
  qtdCaiuCasa = 0
  for i in range(len(apples)):
    apples[i] = apples[i] + a
    #print(apples[i])
    if apples[i] >= s:
      if apples[i] <= t:
        qtdCaiuCasa += 1

  print(qtdCaiuCasa)

  qtdCaiuCasa = 0
  for i in range(len(oranges)):
    oranges[i] = oranges[i] + b
    #print(oranges[i])
    if oranges[i] >= s:
      if oranges[i] <= t:
        qtdCaiuCasa += 1

  print(qtdCaiuCasa)

s, t = input("Distancia da Casa: ").split()
s = int(s)
t = int(t)

a, b = input("Distancia das Arvores: ").split()
a = int(a)
b = int(b)

m, n = input("Qtd de macas e laranjas que cairam: ").split()
m = int(m)
n = int(n)

apples = input("Distancia que as macas cairam ").split()
apples = [int(i) for i in apples]

oranges = input("Distancia que as laranjas cairam ").split()
oranges = [int(i) for i in oranges]

countApplesAndOranges(s,t,a,b,n,m,apples,oranges)