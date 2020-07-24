# from Main.classcode import main as Reg
#
# A = Reg.registers("00")
# B = Reg.registers("00")
# C = Reg.registers("00")
# D = Reg.registers("00")
# E = Reg.registers("00")
# H = Reg.registers("00")
# L = Reg.registers("00")
# M = Reg.registers("00")
# Flag = Reg.registers("00")
# x1 = Reg.registers("00")
#
# BC = Reg.RegPair(B, C)
# DE = Reg.RegPair(D, E)
# HL = Reg.RegPair(H, L)
# PSW = Reg.RegPair(A, Flag)
# PC = Reg.RegPair(x1, x1)
# SP = Reg.StackPointer(Reg.registers("FF"), Reg.registers("FF"))
#
# L.register(HL)
# H.register(HL)
#
# B.register(BC)
# C.register(BC)
#
# D.register(DE)
# E.register(DE)
#
# HL.register(M)
#
# regs = [A, B, C, D, E, H, L, M]
#
#
# def throwreg(n):
#     val = {
#                 "A": A,             # 0
#                 "B": B,             # 1
#                 "C": C,             # 2
#                 "D": D,             # 3
#                 "E": E,             # 4
#                 "H": H,             # 5
#                 "L": L,             # 6
#                 "M": M,             # 7
#                 "PSW": PSW,         # 8
#                 "PC": PC,           # 9
#                 "SP": SP            # 10
#     }
#     return val.get(n)
#
# print(throwreg('A'))
# RegisterPairs = [PSW, BC, DE, HL, SP, PC]
#
# RegPair_Dict = {
#     "B": BC,
#     "D": DE,
#     "H": HL,
#     "SP": SP,
#     "PC": PC,
#     "PSW": PSW
# }
#
# Reg_Dict = {
#                 "A": A,
#                 "B": B,
#                 "C": C,
#                 "D": D,
#                 "E": E,
#                 "H": H,
#                 "L": L,
#                 "M": M
#             }

