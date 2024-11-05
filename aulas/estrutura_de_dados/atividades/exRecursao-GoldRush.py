def verifica(pilhaInicial, resultado):
    if pilhaInicial == resultado:
        return "Yes"
    elif pilhaInicial < resultado:
        return "No"
    else:
        return verifica(desenpilhador(pilhaInicial, 0), resultado)

def desenpilhador(pilha1, pilha2):
    if pilha1 <= 2*pilha2:
        return pilha1
    else:
        return desenpilhador(pilha1-1, pilha2+1)

testes = int(input())
for i in range(testes):
    pilhainicial, resultado = input().split()
    print(verifica(int(pilhainicial), int(resultado)))