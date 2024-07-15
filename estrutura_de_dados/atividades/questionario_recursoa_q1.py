repeticoes = {}
repeticoes[0] = [1,0]
repeticoes[1] = [1,0]
def fibonacci(n):
    if n >= len(repeticoes):
        repeticoes[n] = [fibonacci(n-1)+fibonacci(n-2), 0]
    repeticoes[n][1] += 1
    return repeticoes[n][0]

n = int(input())

print(f"fibonacci({n}) = {fibonacci(n)}")
for i in range(n+1):
    print(f"{repeticoes[i][1]} chamada(s) a fibonacci(" + str(i) +").")