
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


qtdRoupas = int(input())
roupas = input().split()

print(procuraRepetida(roupas))