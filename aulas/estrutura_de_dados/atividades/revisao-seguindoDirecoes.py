def folloingDirections(qtd, direcoes):
    candy = [1, 1]
    alperen = [0, 0]
    for i in range(qtd):
        if direcoes[i] == "L":
            alperen[0] -= 1
        elif direcoes[i] == "R":
            alperen[0] += 1
        elif direcoes[i] == "U":
            alperen[1] += 1
        else:
            alperen[1] -= 1

        if candy[0] == alperen[0] and candy[1] == alperen[1]:
            return True

    return False


qtdCasosTeste = int(input())
for i in range(qtdCasosTeste):
    tamString = int(input())
    direcoes = input()

    if folloingDirections(tamString, direcoes):
        print("YES")
    else:
        print("NO")
