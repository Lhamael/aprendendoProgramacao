def timeConversion(s):
  s = s.upper()
  novo_horario = ''
  if s[8:10]=='PM':
    s = s.replace("PM", "")
    if s[0:2] != "12":
      temp = s[0:2]
      numero = int(s[0:2])+12
      numero = str(numero)
      s = s.replace(temp, numero)
      print(s)
    else:
      print(s)


  elif s[8:10]=='AM':
    s = s.replace("AM", "")
    if s[0:2] != "12":
      print(s)
    else:
      temp = s[0:2]
      numero = "00"
      s = s.replace(temp, numero)
      print(s)

s = input()
timeConversion(s)