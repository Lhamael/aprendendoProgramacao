def bubbleSort(lista, tamanho):
  contador = 0
  for passnum in range(tamanho-1, 0, -1):
    for i in range(passnum):
      if lista[i] > lista[i+1]:
        lista[i], lista[i+1] = lista[i+1], lista[i]
        contador += 1

  return contador

qtdEntrada = int(input())
for i in range(qtdEntrada):
  tamanhoVet = int(input())
  temp = input().split()
  vetor = [int(j) for j in temp]

  print(bubbleSort(vetor, tamanhoVet))
