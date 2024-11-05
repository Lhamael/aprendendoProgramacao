from pythonds.basic.stack import Stack

numero = int(input())

pilha = Stack()
while numero > 0:
    temp = numero%2
    numero = numero//2
    pilha.push(temp)

resultBin = ""
while pilha.isEmpty() != True :
    resultBin += str(pilha.pop())

print(resultBin)

