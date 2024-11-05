def cocaCola(n):
    if n < 2:
        return 0
    elif n == 2:
        return cocaCola(n+1)
    else:
        return n//3 + cocaCola(n//3+n%3)
    
emprestimo = int(input())
i = 0
while emprestimo != 0 or i < 10:
    i+=1
    print(cocaCola(emprestimo))
    emprestimo = int(input())