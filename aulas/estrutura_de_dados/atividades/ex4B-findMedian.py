def merge(esquerda, direita):
  vetor = []
  while esquerda and direita:

    if esquerda[0] <= direita[0]:
      vetor.append(esquerda.pop(0))
    else:
      vetor.append(direita.pop(0))

  if esquerda:
    vetor.extend(esquerda)
  else:
    vetor.extend(direita)

  return vetor

def mergeSort(vetor):
  if len(vetor) < 2:
    return vetor
  meio = len(vetor) // 2
  esquerda = mergeSort(vetor[:meio])
  direita = mergeSort(vetor[meio:])
  return merge(esquerda, direita)


def findMedian(tamArr, arr):
  arr = mergeSort(arr)
  if tamArr%2 != 0:
    mediana = tamArr // 2
    print(arr[mediana])
  else:
    mediana = tamArr // 2
    print((arr[mediana] + arr[mediana-1]) / 2)


tamArr = int(input())
temp = input().split()
arr = [int(i) for i in temp]

findMedian(tamArr, arr)