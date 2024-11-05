def partition(arr, low, high):
  i = low - 1
  pivot = arr[high]
  for j in range(low, high):
      if arr[j] >= pivot:
          i += 1
          arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1

def quickSort(arr, low, high):
  if low < high:
      pi = partition(arr, low, high)
      quickSort(arr, low, pi - 1)
      quickSort(arr, pi + 1, high)
  return arr



def choosingCubes(n, cubosRolados, f, k):
    valFavorito = cubosRolados[f-1]
    #cubosRolados = reverse_merge_sort(n, cubosRolados) #não esquecer de fazer o reverse_merge_sort()
    dadosePosicoes = {}

    cubosRolados = quickSort(cubosRolados, 0, n-1)
    for i in range(n):
        dadosePosicoes[cubosRolados[i]] = []
    for i in range(n):
        dadosePosicoes[cubosRolados[i]].append(i)

    repete=[0,0]
    for i in dadosePosicoes[valFavorito]:
        if i < k:
            repete[0] += 1
        else:
            repete[1] += 1

    if repete[0] > 0 and repete[1] > 0:
        return "MAYBE"
    if repete[0] == 0 and repete[1] > 0:
        return "NO"
    if repete[0] > 0 and repete[1] == 0:
        return "YES"

qtdTestes = int(input())
for i in range(qtdTestes):
    n,f,k = input().split(" ")
    listadecubos = input().split(" ")
    n = int(n)
    f = int(f)
    k = int(k)
    print(choosingCubes(n,listadecubos,f,k))