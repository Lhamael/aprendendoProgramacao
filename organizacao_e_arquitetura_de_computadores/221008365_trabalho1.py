import numpy as np
import struct

mem = np.zeros(16384, dtype=np.uint8)

def lw(reg, kte):
    address = reg + kte;
    if address % 4 == 0:
        return mem[address:address+4].view(dtype = np.uint32)[0]
    else:
        return

def lb(reg, kte):
    address = reg + kte;
    byte = mem[address:address+1].view(dtype = np.int8)[0]
    return np.uint32(byte | 0x00000000)

def lbu(reg, kte):
    address = reg + kte;
    byte = mem[address:address+1].view(dtype = np.uint8)[0]
    return np.uint32(byte | 0x00000000)

def sw(reg, kte, word):
    address = reg + kte;
    if (address % 4) == 0:
        bs = struct.pack('<I', word)
        ba = np.frombuffer(bs, dtype = np.uint8)
        mem[address:address + 4] = ba

def sb(reg, kte, byte):
    address = reg + kte;
    mem[address:address+1] = byte

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
