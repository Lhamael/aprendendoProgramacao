def duplofatorial(n):
    if (n == 0) | (n ==1):
        return 1
    else:
        fatorial = n*duplofatorial(n-2)
        return fatorial
    
def paraString(n,base):
    converteString = "0123456789ABCDEF"
    if n < base:
        return converteString[n]
    else:
        return paraString(n//base, base) + f'{n%base}'

def torreDeHanoi(altura, origem, intermediario, destino):
    if altura >= 1:
        torreDeHanoi(altura-1, origem, destino, intermediario)
        print("Move Disco ", altura, " do pino ", origem, " para o pino ", destino)
        torreDeHanoi(altura-1, intermediario, origem, destino)

torreDeHanoi(5, 'A', 'B', 'C')