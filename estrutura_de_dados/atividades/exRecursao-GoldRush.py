def verifica(pilhaInicial, resultado):
  if pilhaInicial == resultado:
      return True
  if pilhaInicial%3 !=0:
      return False

  return verifica(pilhaInicial//3, resultado) or verifica((pilhaInicial//3)*2, resultado)

testes = int(input())
for i in range(testes):
  pilhainicial, resultado = input().split()
  if verifica(int(pilhainicial), int(resultado)):
    print("Yes")
  else:
    print("No")