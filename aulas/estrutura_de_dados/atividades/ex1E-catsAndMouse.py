"""
x = Gato A
Y = Gato B
Z = Rato C
"""
def catAndMouse(x,y,z):
  catAmouse = abs(x - z)
  catBmouse = abs(y - z)
  if catAmouse == catBmouse:
    print("Mouse C")
  elif catAmouse < catBmouse:
    print("Cat A")
  else:
    print("Cat B")
  return



q = int(input())
i=0
for i in range(q):
  x, y, z = input().split()
  x = int(x)
  y = int(y)
  z = int(z)
  catAndMouse(x,y,z)
