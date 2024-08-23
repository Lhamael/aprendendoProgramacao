def sabacchard(qtdCartas, cartas):
  print(escolhe(cartas, qtdCartas, cartas[0], cartas[qtdCartas-1], 0))
def escolhe(cartas, qtdCartas, primeira, ultima, soma):
  if qtdCartas == 0:
    return soma
  else:
    if primeira > ultima:
      soma += cartas.pop(0)

    elif primeira < ultima:
      soma += cartas.pop()

    else:
      if cartas.peek(1) > cartas.peek(-2):
        soma += cartas.pop(0)

      else:
        soma += cartas.pop()
        
    qtdCartas -= 1
    return descarta(cartas, qtdCartas, cartas[0], cartas[qtdCartas-1], soma)
    
def descarta(cartas, qtdCartas, primeira, ultima, soma):
  if qtdCartas == 0:
    return soma
  else:
    if primeira > ultima:
      cartas.pop()

    elif primeira < ultima:
      cartas.pop(0)

    else:
      if cartas.peek(1) > cartas.peek(-1):
        cartas.pop(0)

      else:
        cartas.pop()

    qtdCartas -= 1
  return escolhe(cartas, qtdCartas, cartas[0], cartas[qtdCartas-1], soma)
    
  

qtdCartas = int(input())
temp = input().split(" ")
cartas = []
cartas.append((int(i) for i in temp))
sabacchard(qtdCartas, cartas)