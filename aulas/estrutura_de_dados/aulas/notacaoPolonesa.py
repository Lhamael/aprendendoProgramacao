"""
Notação polonesa
AB*CD/- => (A*B)-(C/D)
Infixa      posfixa

A ideia do código transformar uma operação infixa e converte-la para posfixa
leia: A+(B*C-(D/E/F)*G)*H
transforme: ABC*DEF//G*-H*+

Como fazer
criar uma pilha das operações
Verifica a ordem de prioridade
Se a prioridade de uma operação for maior ou igual, empilha. Se for menor, desempilha 
a+b/c+d -> A -> | + | -> AB -> | / | -> ABC -> ABC/+ | + | -> ABC/+D -> ABC/+D+
                               | + |
"""
from pythonds.basic.stack import Stack

def notacaoPolonesa(expressao):
    pilha = Stack()
    notacaoPolonesa = []
    i = 0
    for i in range(len(expressao)):
        if expressao[i] == ")" or expressao[i] == "(" or (expressao[i] == "+") or (expressao[i] == "-") or (expressao[i] == "*") or (expressao[i] == "/"):
            if pilha.isEmpty():
                pilha.push(expressao[i])
            else:
                if expressao[i] == ')':
                    while not pilha.isEmpty() and pilha.peek() != '(':
                        notacaoPolonesa.append(pilha.pop())
                    if not pilha.isEmpty() and pilha.peek() == '(':
                        pilha.pop()
                elif (pilha.peek() == '*' or pilha.peek() == '/') and (expressao[i] == '+' or expressao[i] == '-'):
                    while (not pilha.isEmpty()) and (pilha.peek() != '('):
                        notacaoPolonesa.append(pilha.pop())
                    pilha.push(expressao[i])
                else:
                    pilha.push(expressao[i])
        else:
            notacaoPolonesa.append(expressao[i])

    while not pilha.isEmpty():
        notacaoPolonesa.append(pilha.pop())

    print(notacaoPolonesa)


notacaoPolonesa("A+(B*C-(D/E/F)*G)*H")

