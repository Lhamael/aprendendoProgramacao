import numpy as np
import struct

mem = np.zeros(16384, dtype=np.uint8)



"""
#--------------- Exemplo de uso ---------------

sb(7, 0, 0xaa)
word  = lb(7, 0)
print("word_10: ", word)
print("word_x: ", hex(word), "\n")

#---------- Verificação de endereços ----------

sw(0, 0, 0xABACADEF)
sb(4,0,0x1)
sb(4,1,0x2)
sb(4,2,0x3)
sb(4,3,0x4)

print(hex(lw(0, 0)))
print(hex(lb(0, 0)))
print(hex(lb(0, 1)))
print(hex(lb(0, 2)))
print(hex(lb(0, 3)))
print(hex(lbu(0, 0)))
print(hex(lbu(0, 1)))
print(hex(lbu(0, 2)))
print(hex(lbu(0, 3)))
"""
