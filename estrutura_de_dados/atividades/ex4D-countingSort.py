def merge(esquerda, direita):
  vetor = []
  while esquerda and direita:

    if esquerda[0][0] <= direita[0][0]:
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

repeticoes = int(input())
i = 0
arr = []
while i < repeticoes:
  if i < (repeticoes//2):
    temp = input().split()
    temp[0] = int(temp[0])
    temp[1] = '-'
    arr.append(temp)
  else:
    temp = input().split()
    temp[0] = int(temp[0])
    arr.append(temp)
  i+=1

arr = mergeSort(arr)
i = 0
resposta = []
for i in range(repeticoes):
  resposta.append(arr[i][1])
  resultantef =' '.join(str(v) for v in resposta)

print(resultantef)