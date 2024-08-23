def trianguloAmoroso(qtdPlanos, apaixonites):
  for plano in range(qtdPlanos-1):
    achouTrianguloAmoroso = procuraTrianguloAmoroso(plano+1, plano+1, apaixonites[plano], 1, apaixonites)
    if achouTrianguloAmoroso:
      break
  if achouTrianguloAmoroso:
    print("YES")
  else:
    print("NO")

def procuraTrianguloAmoroso(inicial, atual, proximo, qtdLigacoes, apaixonites):
  if qtdLigacoes == 3:
    if proximo == inicial:
      return True
    else:
      return False
  return procuraTrianguloAmoroso(inicial, proximo, apaixonites[proximo-1], qtdLigacoes+1, apaixonites)



n = int(input())
temp = input().split()
f = [int(j) for j in temp]
trianguloAmoroso(n, f)