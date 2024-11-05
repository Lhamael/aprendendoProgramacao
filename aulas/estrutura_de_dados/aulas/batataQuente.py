class BatatQuente:
  def __init__(self) -> None:
    self.fifo = []

  def adiciona(self, crianca):
    self.fifo.append(crianca)

  def roda(self, numero):
    temp = 0
    while len(self.fifo)>0:
      voltas = numero//len(self.fifo)
      voltas = voltas*len(self.fifo)
      voltas = abs(voltas - numero)
      if voltas == 0:
        print(self.fifo.pop())
      else:
        print(self.fifo.pop(voltas-1))

      print(voltas)
      temp = voltas

brincadeira = BatatQuente()
brincadeira.adiciona("Brad")
brincadeira.adiciona("Kent")
brincadeira.adiciona("Bill")
brincadeira.adiciona("David")
brincadeira.adiciona("Susan")
brincadeira.adiciona("Jane")

print(brincadeira)

print(brincadeira.roda(99))


