def plusMinus(n, arr):
  pos = 0
  neg = 0
  zero = 0
  # Verifica a quantidade de argumentos positivos
  for i in range(n):
    if arr[i] > 0:
      pos += 1
    elif arr[i] < 0:
      neg += 1
    else:
      zero += 1

  pos = pos/n
  neg = neg/n
  zero = zero/n
  print(f"{pos:f}\n")
  print(f"{neg:f}\n")
  print(f"{zero:f}\n")

n = int(input("Qtd de valores: "))
elem = input("Valores do vetor: ").split()
arr = [int(val) for val in elem]
erro = False

if n > 0 & n <= 100:
  for i in range(n):
    if arr[i] < -100 & arr[i] > 100:
      erro = True
      break
  if erro == False:
    plusMinus(n, arr)