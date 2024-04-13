def corrida(array):
  valores = [abs(array[0] - array[1]), array[0], array[1]]
  i = 0
  while i<len(array):
    i+=1
    if (abs(array[i] - array[i+1])) == 0:
      valores[0] = 0
      valores[1] = i
      valores[2] = i+1

      return valores


    if (abs(array[i] - array[i+1])) < valores[0]:
      valores[0] = abs(array[i] - array[i+1])
      valores[1] = i
      valores[2] = i+1


  return valores

temp = input().split()
pilotos = [int(i) for i in temp]

resultado = corrida(pilotos)
print(f"A menor diferenca eh: {resultado[0]}\nOs pilotos que tiveram essa difereça foram {resultado[1]} e {resultado[2]}")