repeticoes = {}
repeticoes[0] = 0
repeticoes[1] = 0
def verificaDicionario(n):
    if n in repeticoes:
        repeticoes[n] +=1
    else:
        repeticoes[n] = 1
def fibonacci(n):
    verificaDicionario(n)
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())

print(fibonacci(n))
for i in range(n+1):
    print(repeticoes[i])