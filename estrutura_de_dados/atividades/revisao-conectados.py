from pythonds.basic.stack import Stack
def conectados(posBolinhas, posResultado, n):
    espacoInicial = Stack()
    espacoReservado = Stack()
    listaResult = ""
    for i in range(n):
        espacoInicial.push(posBolinhas[i])

    while not (espacoReservado.isEmpty() and espacoInicial.isEmpty()) and (i > -1):
        if not espacoInicial.isEmpty():
            if espacoInicial.peek() == posResultado[i]:
                espacoInicial.pop()
                listaResult += 'M'
            elif espacoReservado.isEmpty():
                espacoReservado.push(espacoInicial.pop())
                listaResult += 'G'

            elif espacoReservado.peek() == posResultado[i]:
                espacoReservado.pop()
                listaResult += 'R'
            else:
                return "Defeito de fabrica!"
        else:
            if not espacoReservado.isEmpty() and espacoReservado.peek() == posResultado[i]:
                espacoReservado.pop()
                listaResult += 'R'
            elif not espacoReservado.isEmpty() and espacoReservado.peek() != posResultado[i]:
                return "Defeito de fabrica!"
            else:
                break
        i -= 1
    return listaResult

qtdCores = int(input())
bolinhas = input().split(' ')
resultado = input().split(' ')
print(conectados(bolinhas, resultado, qtdCores))





