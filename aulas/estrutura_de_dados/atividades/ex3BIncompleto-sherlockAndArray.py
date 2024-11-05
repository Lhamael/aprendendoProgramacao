def balancedSums(vetor, termVetor):
  meio = 0
  somPriMetade = 0
  somSegMetade = 0
  if termVetor > 1:
    while meio < termVetor:
      for x in range(meio):
        somPriMetade += vetor[x]

      for x in range(meio+1, termVetor):
        somSegMetade += vetor[x]

      if somPriMetade == somSegMetade:
        return "YES"
      else:
        somPriMetade = 0
        somSegMetade = 0
        meio += 1

    return "NO"

  elif termVetor == 1:
    return "YES"
  else:
    return "NO"



T = int(input())
validador = True
if T>=1 and T<=10:
  for i in range(T):
    n = int(input())
    temp = input().split()
    arr = [int(j) for j in temp]
    if (n>=1 and n<=100000) and (i>=0 and i<n):
      for j in arr:
        if not(j>=0 and j<=20000):
          validador = False
          break
      if validador:
        resposta = balancedSums(arr, n)
        print(resposta)
    validador =  True