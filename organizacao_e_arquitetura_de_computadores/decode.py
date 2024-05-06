import numpy as np

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

    ic["ins_code"] = get_instr_code(ic["opcode"], ic["funct3"], ic["funct7"])
    ic["ins_format"] = get_i_format(ic["opcode"], ic["funct3"], ic["funct7"])
    ic["rs1"] = REGISTERS(ic["rs1"])
    ic["rs2"] = REGISTERS(ic["rs2"])
    ic["rd"] = REGISTERS(ic["rd"])

    return ic
