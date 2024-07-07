    """
        se for b, deleta a ultima letra minuscula, ou se for B, deleta a ultima letra maiscula.
        como fazer: Implementar duas pilhas, se for b ou B, a primeira pilha, vai passar elemento a elemento procurando
                    a letra correspondente a logica para deletar, ao achar,retira a letra da pilha e passa o restantes
                    da pilha para a outra pilha e essa outra pilha devolve para a string.
    """
    from pythonds.basic.stack import Stack
    def yetnotherrokenKeoard(vetor):
        output = ""
        pilha1 = Stack()
        pilha2 = Stack()

        """ # Desta forma dá certo, mas tem outra forma que também dá certo
        
        verificador = False
        for i in vetor:
            if vetor[i] == "b":
                for j in output:
                    if (ord(j)<97 or ord(j)>122) or verificador:
                        pilha1.push(output[i])
                    else:
                        verificador = True
                output = ''
                while not pilha1.isEmpty():
                    pilha2.push(pilha1.pop())
                while not pilha2.isEmpty():
                    output += pilha2.pop()
    
               
            elif vetor[i] == "B":
                for j in output:
                    if (ord(j)<65 or ord(j)>90) or verificador:
                        pilha1.push(output[i])
                    else:
                        verificador = True
                output = ''
                while not pilha1.isEmpty():
                    pilha2.push(pilha1.pop())
                while not pilha2.isEmpty():
                    output += pilha2.pop()
    
            else:
                output += vetor[i]
    """
        for i in vetor:
            if i == "B":
                while not pilha1.isEmpty():
                    if (ord(pilha1.peek())<65 or ord(pilha1.peek())>90):
                        pilha2.push(pilha1.pop())
                    else:
                        pilha1.pop()
                        break
                while not pilha2.isEmpty():
                    pilha1.push(pilha2.pop())

            elif i == "b":
                while not pilha1.isEmpty():
                    if (ord(pilha1.peek())<97 or ord(pilha1.peek())>122):
                        pilha2.push(pilha1.pop())
                    else:
                        pilha1.pop()
                        break
                while not pilha2.isEmpty():
                    pilha1.push(pilha2.pop())

            else:
                pilha1.push(i)

        while not pilha1.isEmpty():
            pilha2.push(pilha1.pop())
        while not pilha2.isEmpty():
            output += pilha2.pop()
        return output

    repeticoes = int(input())
    for i in range(repeticoes):
        digitado = input()
        print(yetnotherrokenKeoard(digitado))