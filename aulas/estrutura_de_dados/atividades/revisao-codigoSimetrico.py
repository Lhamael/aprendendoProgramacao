def binarySearch(arr, item):

    first = 0
    last = len(arr) - 1
    while first <= last:
        middle = (first + last) // 2
        if arr[middle] == item:
            return middle
        elif ord(arr[middle]) < ord(item):
            first = middle + 1

        else:
            last = middle - 1
    return -1
        
def merge(esquerda, direita):
    vetor = []

    while esquerda and direita:
        if esquerda[0] <= direita[0]:
            vetor.append(esquerda.pop(0))
        else:
            vetor.append(direita.pop(0))

    if esquerda:
        vetor.extend(esquerda)
    if direita:
        vetor.extend(direita)

    return vetor

def merge_sort(vetor):
    if len(vetor) < 2:
        return vetor
    meio = len(vetor) //2
    esquerda = merge_sort(vetor[:meio])
    direita = merge_sort(vetor[meio:])
    return merge(esquerda, direita)



def symmetricEncoding(qtdCarac, palavra):
    dicionario = {}
    r=[]
    resposta = ""
    for i in palavra:
        dicionario[i] = 0

    for i in dicionario:
        r.append(i)

    r = merge_sort(r)

    for i in range(qtdCarac):
        posiLetra = binarySearch(r,palavra[i])
        resposta += r[(len(r)-posiLetra)-1]

    return resposta

repeticoes = int(input())
for i in range(repeticoes):
    qtdcaracteres = int(input())
    palavra = input()
    resposta = symmetricEncoding(qtdcaracteres, palavra)
    print(resposta)
