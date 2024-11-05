#Aqui, veremos alguns algoritmos de ordenação
#Bubble Sort
def bubble_sort(vetor):
  for passnum in range(len(vetor) - 1, 0, -1):
    for i in range(passnum):
      if vetor[i] > vetor[i + 1]:
        vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]

  # Complexidade espacial: O(1)
  # Performance no melhor caso: O(n)? Array já ordenado
  # Performance no caso médio: O(n^2) Array ordenado aleatoriamente
  # Performance no pior caso: O(n^2) Array ordenado ao contrário
  
  #----------------------------------------------------------------------#

# Selection Sort
def selection_sort(vetor):
  n = len(vetor)
  for i in range(n):
      min_idx = i
      for j in range(i + 1, n):
          if vetor[j] < vetor[min_idx]:
              min_idx = j
      vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]
  return vetor

  # Complexidade espacial: O(1)
  # Performance no melhor caso: O(n^2) Array já ordenado
  # Performance no caso médio: O(n^2) Array ordenado aleatoriamente
  # Performance no pior caso: O(n^2) Array ordenado ao contrário
  
  #----------------------------------------------------------------------#

# Inserction Sort
def insertion_sort(arr):
  for i in range(1, len(arr)):
      key = arr[i]
      j = i - 1
      while j >= 0 and key < arr[j]:
          arr[j + 1] = arr[j]
          j -= 1
      arr[j + 1] = key
  return arr

  # Complexidade espacial: O(1)
  # Performance no melhor caso: O(n) Array já ordenado
  # Performance no caso médio: O(n^2) Array ordenado aleatoriamente
  # Performance no pior caso: O(n^2) Array ordenado ao contrário

  #----------------------------------------------------------------------#

# Merge Sort
def merge_sort(arr):
  if len(arr) > 1:
      mid = len(arr) // 2
      L = arr[:mid]
      R = arr[mid:]
      merge_sort(L)
      merge_sort(R)
      i = j = k = 0
      while i < len(L) and j < len(R):
          if L[i] < R[j]:
              arr[k] = L[i]
              i += 1
          else:
              arr[k] = R[j]
              j += 1
          k += 1
      while i < len(L):
          arr[k] = L[i]
          i += 1
          k += 1
      while j < len(R):
          arr[k] = R[j]
          j += 1
          k += 1
  return arr

  # Complexidade espacial: O(n)
  # Performance no melhor caso: O(n log n) Array já ordenado
  # Performance no caso médio: O(n log n) Array ordenado aleatoriamente
  # Performance no pior caso: O(n log n) Array ordenado ao contrário

  #----------------------------------------------------------------------#

# Quick Sort
def partition(arr, low, high):
  i = low - 1
  pivot = arr[high]
  for j in range(low, high):
      if arr[j] <= pivot:
          i += 1
          arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1

def quick_sort(arr, low, high):
  if low < high:
      pi = partition(arr, low, high)
      quick_sort(arr, low, pi - 1)
      quick_sort(arr, pi + 1, high)
  return arr

  # Complexidade espacial: O(n log n) a O(n) ?
  # Performance no melhor caso / caso médio: O(n log n) Quando o prticionamento sempre pega o elemento do meio
  # Performance no pior caso: O(n^2) Quando o prticionamento sempre pega as extremidades
  
  #----------------------------------------------------------------------#
  
# Counting Sort
def counting_sort(arr):
  n = len(arr)
  output = [0] * n
  count = [0] * 256
  for i in range(n):
      count[ord(arr[i])] += 1
  for i in range(1, 256):
      count[i] += count[i - 1]
  for i in range(n):
      output[count[ord(arr[i])] - 1] = arr[i]
      count[ord(arr[i])] -= 1
  for i in range(n):
      arr[i] = output[i]
  return arr

  # Complexidade espacial: O(n + k), onde k é o range dos elementos a serem ordenados
  # Performance: O(n)
