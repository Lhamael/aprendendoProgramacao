#resposta incorreta
from pythonds import Queue
def contaBuracos(linhas, colunas, parede, verificador):
    qtdBuracos = 0
    proxLinha = Queue()
    proxColuna = Queue()
    proxColuna.enqueue(0)
    proxLinha.enqueue(0)
    verificador[0][0] = True
    while not proxColuna.isEmpty():
        linhaAtual = proxLinha.dequeue()
        colunaAtual = proxColuna.dequeue()
        if parede[linhaAtual][colunaAtual] == ".":
            qtdBuracos += 1

        def estaForaDoLimite(proxLinha, proxColuna):
            if proxLinha < 0 or proxLinha > linhas-1:
                return False
            if proxColuna < 0 or proxColuna > colunas-1:
                return False
            return True

        def foiVerificado(proxLinha, proxColuna):
            if verificador[proxLinha][proxColuna]:
                return True
            return False

        verificaLinha = linhaAtual
        verificaColuna = colunaAtual+1
        if estaForaDoLimite(verificaLinha, verificaColuna):
            if not foiVerificado(verificaLinha, verificaColuna):
                proxLinha.enqueue(verificaLinha)
                proxColuna.enqueue(verificaColuna)
                verificador[verificaLinha][verificaColuna] = True

        verificaLinha = linhaAtual+1
        verificaColuna = colunaAtual
        if estaForaDoLimite(verificaLinha, verificaColuna):
            if not foiVerificado(verificaLinha, verificaColuna):
                proxLinha.enqueue(verificaLinha)
                proxColuna.enqueue(verificaColuna)
                verificador[verificaLinha][verificaColuna] = True

        verificaLinha = linhaAtual
        verificaColuna = colunaAtual-1
        if estaForaDoLimite(verificaLinha, verificaColuna):
            if not foiVerificado(verificaLinha, verificaColuna):
                proxLinha.enqueue(verificaLinha)
                proxColuna.enqueue(verificaColuna)
                verificador[verificaLinha][verificaColuna] = True

        verificaLinha = linhaAtual-1
        verificaColuna = colunaAtual
        if estaForaDoLimite(verificaLinha, verificaColuna):
            if not foiVerificado(verificaLinha, verificaColuna):
                proxLinha.enqueue(verificaLinha)
                proxColuna.enqueue(verificaColuna)
                verificador[verificaLinha][verificaColuna] = True

    print(qtdBuracos)


n,m = list(map(int, input().split()))
parede = []
verificador = [[False for j in range(m)] for i in range(n)]
contador = 0
for i in range(n):
    parede.append(list(input()))
    if '.' in parede[i]:
        contador += 1
print(contador)
#contaBuracos(n, m, parede, verificador)