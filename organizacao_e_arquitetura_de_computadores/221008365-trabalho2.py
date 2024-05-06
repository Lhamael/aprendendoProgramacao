import numpy as np
import struct

# Primeiro, definimos o tamanho da memória que utilizaremos para ler o code e o data binários do assembly
mem = np.zeros(16384, dtype=np.uint8)

# Função que lê um codigo .bin e carrega em code
with open('code.bin', 'rb') as f:
    code = np.frombuffer(f.read(), dtype=np.uint8)

# Função que lê um data .bin e carrega em data
with open('data.bin', 'rb') as f:
    data = np.frombuffer(f.read(), dtype=np.uint8)

# Função que carrega o code e o data na memória
def load_mem():
    mem[0:len(code)] = code
    mem[16384-len(data):16384] = data

# Funções lb, lw, lbu, sw e sb criadar no trabalho 1
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

def sw(reg, kte, dado):
    address = reg + kte;
    if (address % 4) == 0:
        bs = struct.pack('<I', dado)
        ba = np.frombuffer(bs, dtype = np.uint8)
        mem[address:address + 4] = ba

def sb(reg, kte, dado):
    address = reg + kte;
    mem[address:address+1] = dado

# Valores inicias dos registradores
pc = np.uint32(0)
ri = np.uint32(0)
sp = np.uint32(0x3ffc)
gp = np.uint32(0x1800)

# Define a função Fetch, que busca as instruções a serem usadas na memória e utiliza PC
def fetch():
    global pc, ri
    ri = lw(pc, 0)
    pc += 4

# Função que extrai todos os campos de instrução e define o formato e o código da instrução
def decode(ri):
    ic = np.zeros(1, dtype=[
        ("opcode", np.uint32),
        ("rs2", np.uint32),
        ("rs1", np.uint32),
        ("rd", np.uint32),
        ("shamt", np.uint32),
        ("funct3", np.uint32),
        ("funct7", np.uint32),
        ("imm12_i", np.int32),
        ("imm12_s", np.int32),
        ("imm13", np.int32),
        ("imm21", np.int32),
        ("imm20_u", np.uint32)
    ])[0]

    ic["opcode"] = ri & 0x7F
    ic["rs2"] = (ri >> 20) & 0x1F
    ic["rs1"] = (ri >> 15) & 0x1F
    ic["rd"] = (ri >> 7) & 0x1F
    ic["shamt"] = (ri >> 20) & 0x1F
    ic["funct3"] = (ri >> 12) & 0x7
    ic["funct7"] = ri >> 25
    ic["imm12_i"] = np.int32(ri) >> 20
    tmp = (ri & 0x1F)
    ic["imm12_s"] = np.int32((ic["imm12_i"] & 0xFFFFF) | (tmp << 5))
    ic["imm13"] = ic["imm12_s"]
    ic["imm13"] |= (ic["imm13"] & 1) << 11
    ic["imm13"] &= ~1
    ic["imm20_u"] = ri & (~0xFFF)

    imm21 = np.int32(ri) >> 11
    tmp = (ri >> 12) & 0xFF
    imm21 |= tmp << 12
    tmp = (ri >> 20) & 1
    imm21 |= tmp << 11
    tmp = (ri >> 21) & 0x3FF
    imm21 |= tmp << 1
    imm21 &= ~1
    ic["imm21"] = imm21
"""
    ic["ins_code"] = get_instr_code(ic["opcode"], ic["funct3"], ic["funct7"])
    ic["ins_format"] = get_i_format(ic["opcode"], ic["funct3"], ic["funct7"])
    ic["rs1"] = REGISTERS(ic["rs1"])
    ic["rs2"] = REGISTERS(ic["rs2"])
    ic["rd"] = REGISTERS(ic["rd"])

    return ic
"""

# Função que executa a instrução que foi lida pela função fetch() e decodifica para decode()
def execute():
    global pc, ri
    ic = decode(ri)
    print(ic)

# Função que executa uma instrução do Risc V linha por linha
def step():
    fetch()
    execute()

# Função que executa o programa até encontrar uma chamada de sistema para encerrar ou até o pc utrapassa o limite de 2000 words
def run():
    global pc
    while pc < 2000:
        step()

# Implementação das instruções bases do Risc V
# Add
def add(rs1, rs2):
    return rs1 + rs2

# Sub
def sub(rs1, rs2):
    return rs1 - rs2

# And
def and_(rs1, rs2):
    return rs1 & rs2

# Andi
def and_i(rs1, imm):
    return rs1 & imm

# Auipc
def auipc(imm):
    return pc + imm

# Beq
def beq(rs1, rs2, imm):
    if rs1 == rs2:
        return pc + imm
    else:
        return pc + 4

# Bne
def bne(rs1, rs2, imm):
    if rs1 != rs2:
        return pc + imm
    else:
        return pc + 4

# Bgeu
def bgeu(rs1, rs2, imm):
    if rs1 >= rs2:
        return pc + imm
    else:
        return pc + 4

# Blt
def blt(rs1, rs2, imm):
    if rs1 < rs2:
        return pc + imm
    else:
        return pc + 4

# Bltu
def bltu(rs1, rs2, imm):
    if rs1 < rs2:
        return pc + imm
    else:
        return pc + 4

# Jal
def jal(imm):
    return pc + imm

# Jalr
def jalr(imm):
    return pc + imm

# Lb
def lb(rs1, imm):
    return rs1 + imm

# Or
def or_(rs1, rs2):
    return rs1 | rs2

# Lbu
def lbu(rs1, imm):
    return rs1 + imm

# Lui
def lui(imm):
    return imm

# Slt
def slt(rs1, rs2):
    if rs1 < rs2:
        return 1
    else:
        return 0

# Sltu
def sltu(rs1, rs2):
    if rs1 < rs2:
        return 1
    else:
        return 0

# Ori
def ori(rs1, imm):
    return rs1 | imm

# Sb
def sb(rs1, imm):
    return rs1 + imm

# Slli
def slli(rs1, imm):
    return rs1 << imm

# Srai
def srai(rs1, imm):
    return rs1 >> imm

# Srli
def srli(rs1, imm):
    return rs1 >> imm

# Sub
def sub(rs1, rs2):
    return rs1 - rs2

# Sw
def sw(rs1, imm):
    return rs1 + imm

# Xor
def xor(rs1, rs2):
    return rs1 ^ rs2

# Xori
def xori(rs1, imm):
    return rs1 ^ imm

# Ecall - simula a função Syscall do rasr/riscv
def ecall(rs1, rd):
    if rs1 == 1:
        print("Valor inteiro:", rd)
    elif rs1 == 2:
        print("Valor float:", rd)
    elif rs1 == 3:
        print("Valor double:", rd)
    elif rs1 == 4:
        print("String:", rd)
    elif rs1 == 5:
        rd = int(input("Digite um valor inteiro: "))
        return rd
    elif rs1 == 6:
        rd = float(input("Digite um valor float: "))
        return rd
    elif rs1 == 7:
        rd = float(input("Digite um valor double: "))
        return rd
    elif rs1 == 8:
        rd = input("Digite uma string: ")
        return rd
    elif rs1 == 9:
        print("Memória alocada na heap")
    elif rs1 == 10:
        print("Encerrando código")
    elif rs1 == 11:
        print("Caractere ASCII:", chr(rd))
    elif rs1 == 12:
        rd = input("Digite um caractere: ")
        return rd

