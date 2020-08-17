from Main.Objects import flags
from Main.hexadecimals import hexconvs
from Main.Database import Db as dbfuncs


class registers:
    def __init__(self, s):
        self.reg = s
        self.length = len(s)
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def dispatch(self):
        for s in self.subscribers:
            s.update_pair(self)

    def __add__(self,other):
        c1 = "0x" + str(self.reg)
        c2 = "0x" + str(other.reg)

        v1 = int(c1, 16) + int(c2, 16)
        flags.flag['CY'] = 1 if v1 > 255 else 0
        self.reg = hexconvs.int2hexstr(v1)
        return self

    def __sub__(self, other):
        c1 = "0x" + str(self.reg)
        c2 = "0x" + str(other.reg)
        res = int("0xFF", 16) + int(c1, 16) - int(c2, 16)+1
        flags.flag['CY'] = 0 if int(c1, 16) >= int(c2, 16) else 1
        self.reg = hexconvs.int2hexstr(res)
        return self
    
    def __and__(self,other):
        c1 = "0x"+str(self.reg)
        c2 = "0x"+str(other.reg)
    
        v1 = int(c1,16)&int(c2,16)
        flags.flag['CY'] = 1 if v1>255 else 0
        self.reg = hexconvs.int2hexstr(v1)
        return self

    def __or__(self,other):
        c1 = "0x" + str(self.reg)
        c2 = "0x" + str(other.reg)
    
        v1 = int(c1,16) | int(c2,16)
        flags.flag['CY'] = 1 if v1>255 else 0
        self.reg = hexconvs.int2hexstr(v1)
        return self

    def __xor__(self,other):
        c1 = "0x" + str(self.reg)
        c2 = "0x" + str(other.reg)
    
        v1 = int(c1,16) ^ int(c2,16)
        flags.flag['CY'] = 1 if v1>255 else 0
        self.reg = hexconvs.int2hexstr(v1)
        return self

    def update(self, val):
        self.reg = val
        self.length = len(val)
        self.dispatch()

    def updateObj(self, other):
        self.reg = other.reg
        self.length = other.length
        self.dispatch()

    def update_from_mem(self, addr):
        self.reg = dbfuncs.retrieve_from_memory(addr)
        self.dispatch()
        
    def __str__(self):
        return self.reg

    def binary(self):
        c1 = "0x" + str(self.reg)
        c1 = int(c1, 16)
        return bin(c1)[2:].zfill(8)


# Register Pairs Class

class RegPair:
    def __init__(self, obj1, obj2):
        self.reg = obj1.reg+obj2.reg
        self.length = obj1.length+obj2.length
        self.o1 = obj1
        self.o2 = obj2
        self.subscriber = set()

    def register(self, who):
        self.subscriber.add(who)

    def dispatch(self):
        for s in self.subscriber:
            s.update_mem(self.reg)

    def update(self,obj1,obj2):
        self.reg = obj1.reg+obj2.reg
        self.o1 = obj1
        self.o2 = obj2
        self.length = obj1.length+obj2.length

    def updatePSW(self, obj1, flag):
        flaglist = [str(flag[i]) for i in flag]
        flagRegister = ''.join(flaglist)
        self.o1 = obj1
        self.o2 = registers(flagRegister)
        self.length = 8

    def update_pair(self, other):
        if self.o1 == other:
            self.reg = other.reg + self.reg[2:]
        else:
            self.reg = self.reg[:2] + other.reg

    def updateFromString(self, other):
        self.reg = other
        self.length = 4

    def __str__(self):
        return self.reg

    def mov(self,val):
        self.reg = val
        self.o1.update(val[:2])
        self.o2.update(val[2:])

    def __sub__(self, other):
        v1 = int("0xFFFF",16) + int(self.reg, 16) - int(other.reg, 16) + 1
        self.reg = hex(v1)[2:].zfill(4).upper()
        self.reg = self.reg[-4:]
        self.o2.update(self.reg[2:])
        self.o1.update(self.reg[:2])
        flags.flag['CY'] = 1 if other.reg >= self.reg else 0
        return self
        
    def __add__(self,other):
        result = int(self.reg, 16) + int(other.reg, 16)
        cy = 1 if result > 65535 else 0
        res = hex(result)[2:].zfill(4).upper()
        self.reg = res[-4:]
        self.o2.update(self.reg[2:])
        self.o1.update(self.reg[:2])
        flags.flag['CY'] = cy
        return self


class StackPointer(RegPair):
    def __init__(self, obj1, obj2):
        super().__init__(obj1, obj2)

    def push(self, reg):
        if not isinstance(reg, str):
            reg = reg.reg
        try:
            dcr = int(self.reg,16) - 1
            self.reg = hex(dcr)[2:].upper()
            dbfuncs.store_value_to_memory(self.reg, reg[:2])
            dbfuncs.MemoryTransition[self.reg] = reg[:2]
            self.reg = hex(dcr - 1)[2:].upper()
            dbfuncs.store_value_to_memory(self.reg, reg[2:4])
            dbfuncs.MemoryTransition[self.reg] = reg[2:4]
        except Exception:
            print("cbxjhnv hcvb")

    def pop(self):
        low, high = '', ''
        try:
            inr = int(self.reg, 16)
            self.reg = hex(inr)[2:].upper()
            low = dbfuncs.retrieve_from_memory(self.reg)
            self.reg = hex(inr + 1)[2:].upper()
            high = dbfuncs.retrieve_from_memory(self.reg)
            self.reg = hex(inr + 2)[2:].upper()
        except Exception:
            print("cbxjhnv hcvb")
        val = high + low
        return val


A = registers("00")
B = registers("00")
C = registers("00")
D = registers("00")
E = registers("00")
H = registers("00")
L = registers("00")
M = registers("00")
Flag = registers("00")
x1 = registers("00")

BC = RegPair(B, C)
DE = RegPair(D, E)
HL = RegPair(H, L)
PSW = RegPair(A, Flag)
PC = RegPair(x1, x1)
SP = StackPointer(registers("FF"), registers("FF"))

A.register(PSW)

L.register(HL)
H.register(HL)

B.register(BC)
C.register(BC)

D.register(DE)
E.register(DE)

HL.register(M)

regs = [A, B, C, D, E, H, L, M]


def throwreg(n):
    val = {
                "A": A,             # 0
                "B": B,             # 1
                "C": C,             # 2
                "D": D,             # 3
                "E": E,             # 4
                "H": H,             # 5
                "L": L,             # 6
                "M": M,             # 7
                "PSW": PSW,         # 8
                "PC": PC,           # 9
                "SP": SP            # 10
    }
    return val.get(n)


RegisterPairs = [PSW, BC, DE, HL, SP, PC]

RegPair_Dict = {
    "B": BC,
    "D": DE,
    "H": HL,
    "SP": SP,
    "PC": PC,
    "PSW": PSW
}

Reg_Dict = {
                "A": A,
                "B": B,
                "C": C,
                "D": D,
                "E": E,
                "H": H,
                "L": L,
                "M": M
            }
