def game(colunas, linha1, linha2):
    if colunas == 1:
        return "YES"
    else:
        if linha1[1] == '1' and linha2[1] == '1':
            return "NO"
        else:
            return game(colunas-1, linha1[1:], linha2[1:])

testes = int(input())
for i in range(testes):
    colunas = int(input())
    linha1 = input()
    linha2 = input()
    print(game(colunas, linha1, linha2))