def gcd(a,b): #MDC(a,b)
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def maximize(x):
    maximo = 0
    maiorY = 0
    for y in range(1,x):
        mdc = gcd(y, x)
        soma = mdc + y
        if soma > maximo:
            maximo = soma
            maiorY = y
    return maiorY

repeticoes = int(input())
for i in range(repeticoes):
    print(maximize(int(input())))
