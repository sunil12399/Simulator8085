from Main.classcode.main import *
from Main.Database import Db as dbfuncs
from Main.hexadecimals import cmp
from Main.Objects import flags
from collections import deque
from CustomExceptions import *
import re


def checkNone(value):
    if not value is None:
        raise NotNoneError
    return


def check8bit(value):
    if not re.match(r'[0-9A-H][0-9A-H]', value) or len(value) != 2:
        raise Hexadecimal8bitValueError("Invalid Literal for 8-bit hex value: " + value)
    return


def check16bit(value):
    if not re.match(r'[0-9A-H]{4}', value) or len(value) != 4:
        raise Hexadecimal16bitValueError("Invalid Literal for 16-bit hex value " + value)
    return


def checkreg(var):
    if not re.match(r'[ABCDEHLM]', var):
        raise RegisterError
    return


def checkregpair(var, list=None):
    if list is None:
        list = ["B", "D", "H", "SP"]
    if not var in list:
        raise RegisterError
    return


def checkreg8bitvalue(var):
    if not re.match(r'^\w,[0-9A-H]{2}$',var):
        raise LexicalException("The code must be written in \"Register,Value\" format.")


def checkregreg(var):
    if not re.match(r'^\w,\w$',var):
        raise LexicalException("The code must be written in \"Register,Register\" format.")


def checkreg16bitvalue(var):
    if not re.match(r'^\w+,[0-9A-H]{4}$',var):
        raise LexicalException("The code must be written in \"Register,Value\" format.")


def instructonInterpret(ins, val=None):
    tmp = ""

    if ins == "ADD":
        checkreg(val)
        A = eval('A') + eval(val)
        flags.setFlags(A)

    elif ins == "ADI":
        check8bit(val)
        A = eval('A') + registers(val)
        flags.setFlags(A)

    elif ins == "ACI":
        check8bit(val)
        val = int(val) + int(flags.flag['CY'])
        A = eval('A') +  registers(val)
        flags.flag['CY'] = 0
        flags.setFlags(A)

    elif ins == "ADC":
        checkreg(val)
        value = str(flags.flag['CY'])
        temp = eval(val) + registers(value)
        A = eval('A') + temp
        flags.flag['CY'] = 0
        flags.setFlags(A)

    elif ins == "ANA":
        checkreg(val)
        A = eval('A') & eval(val)
        flags.flag['CY'] = 0
        flags.flag['AC'] = 1
        flags.setFlags(A)

    elif ins == "ANI":
        check8bit(val)
        A = eval('A') & registers(val)
        flags.flag['CY'] = 0
        flags.flag['AC'] = 1
        flags.setFlags(A)

    elif ins == "CMA":
        checkNone(val)
        tmp = registers("FF")
        tmp -= throwreg("A")
        A = eval('A').update(tmp.reg)

    elif ins == "CMC":
        checkNone(val)
        c = flags.flag['CY']
        flags.flag['CY'] = 0 if c else 1

    elif ins == "CMP":
        checkreg(val)
        cmp.comp().hexcmp(eval('A'), eval(val))
    elif ins == "CPI":
        check8bit(val)
        cmp.comp().hexcmp(eval('A'), registers(val))

    elif ins in ['CALL', 'CC', 'CM', 'CNC', 'CP', 'CPE', 'CPO', 'CZ', 'CNZ']:
        if ins == "CNC":
            if flags.flag['CY'] == 0:
                return "goto"
            else:
                return "continue"
        if ins == "CALL":
            return "goto"
        elif ins == "CC" and flags.flag['CY'] == 1:
            return "goto"
        elif ins == "CZ" and flags.flag['Z'] == 1:
            return "goto"
        elif ins == "CNZ" and flags.flag['Z'] == 0:
            return "goto"
        elif ins == "CP" and flags.flag['S'] == 0:
            return "goto"
        elif ins == "CPO" and flags.flag['P'] == 0:
            return "goto"
        elif ins == "CM" and flags.flag['S'] == 1:
            return "goto"
        elif ins == "CPE" and flags.flag['P'] == 1:
            return "goto"
        else:
            return "continue"

    elif ins == "DAA":
        checkNone(val)
        low = int(str(eval('A'))[-1], 16)
        if flags.flag['AC'] or low>9:
            low = low+6
            flags.flag['AC'] = 1 if low >15 else 0
        high = int(str(throwreg('A'))[-2], 16)
        if flags.flag['CY'] or high>9:
            high = high + 6 + flags.flag['AC']
            flags.flag['CY'] = 1 if high>15 else 0
        high = hex(high)[2:]
        low = hex(low)[2:]
        throwreg('A').update(high.upper() + low.upper())
        pass

    elif ins == "DAD":
        checkregpair(val)
        HL = eval('HL') + RegPair_Dict[val]

    elif ins == "DCR":
        checkreg(val)
        x1 = throwreg(val)
        x1 -= registers("01")
        z = flags.flag['CY']
        flags.setFlags(x1)
        flags.flag['CY'] = z

    elif ins == "DCX":
        checkregpair(val)
        i = regs.index(throwreg(val))
        if i == 1:
            tmp = eval('BC')
            tmp.update(B, C)
        elif i == 3:
            tmp = eval('DE')
            tmp.update(D, E)
        elif i == 5:
            tmp = eval('HL')
            tmp.update(H, L)
        z = flags.flag['CY']
        tmp = tmp - RegPair(registers('00'), registers('01'))
        flags.flag['CY'] = z
        if i == 5:
            tmp.dispatch()

    elif ins == "DI":
        pass
    elif ins == "EI":
        pass
    elif ins == "HLT":
        raise EndException("End of program")
        pass
    elif ins == "IN":
        check8bit(val)

    elif ins == "INR":
        checkreg(val)
        x1 = eval(val)
        x1 += registers("01")
        z = flags.flag['CY']
        flags.setFlags(x1)
        flags.flag['CY'] = z

    elif ins == "INX":
        checkregpair(val)
        i = regs.index(throwreg(val))
        if i == 1:
            tmp = eval('BC')
            tmp.update(B, C)
        elif i == 3:
            tmp = eval('DE')
            tmp.update(D, E)
        elif i == 5:
            tmp = eval('HL')
            tmp.update(H, L)
        z = flags.flag['CY']
        rp = RegPair(registers('00'), registers('01'))
        tmp = tmp + rp
        flags.flag['CY'] = z
        if i == 5:
            tmp.dispatch()

    elif ins in ['JC', 'JM', 'JMP', 'JNC', 'JNZ', 'JP', 'JPE', 'JPO', 'JZ']:
        if ins == "JNC":
            if flags.flag['CY'] == 0:
                return "iterate"
            else:
                return "STOP LOOP"
        if ins == "JMP":
            return "iterate"
        elif ins == "JC" and flags.flag['CY'] == 1:
            return "iterate"
        elif ins == "JZ" and flags.flag['Z'] == 1:
            return "iterate"
        elif ins == "JNZ" and flags.flag['Z'] == 0:
            return "iterate"
        elif ins == "JP" and flags.flag['S'] == 0:
            return "iterate"
        elif ins == "JPO" and flags.flag['P'] == 0:
            return "iterate"
        elif ins == "JM" and flags.flag['S'] == 1:
            return "iterate"
        elif ins == "JPE" and flags.flag['P'] == 1:
            return "iterate"
        else:
            return "STOP LOOP"

    elif ins == "LDA":
        check16bit(val)
        eval('A').update(dbfuncs.retrieve_from_memory(val))

    elif ins == "LDAX":
        checkregpair(val,["B","D"])
        i = regs.index(throwreg(val))
        if i == 1:
            tmp = eval('BC')
            tmp.update(B, C)
        elif i == 3:
            tmp = eval('DE')
            tmp.update(D, E)
        A = dbfuncs.retrieve_from_memory(tmp.reg)

    elif ins == "LHLD":
        check16bit(val)
        L.update(dbfuncs.retrieve_from_memory(val))
        val = int(val, 16) + 1
        val = dbfuncs.return_address(val)
        H.update(dbfuncs.retrieve_from_memory(val))
        eval('HL').dispatch()

    elif ins == "LXI":
        temp2 = val.split(',')
        check16bit(temp2[1])        # check the 16 bit value entered
        checkregpair(temp2[0])      # Check the validity of the register
        checkreg16bitvalue(val)     # Check the format Register,0000H here
        tmp = RegPair_Dict[temp2[0]]
        tmp.mov(temp2[1])
        if temp2[0] == 'H':
            tmp.dispatch()

    elif ins == "MOV":
        temp2 = val.split(',')
        checkreg(temp2[0])
        checkreg(temp2[1])
        if temp2[0] == "M" and temp2[1] == "M":
            raise Exception("MOV M,M is not an instruction.")
        if throwreg(temp2[1]) == M:
            HL = str(RegPair_Dict["H"])
            memory_content = dbfuncs.retrieve_from_memory(HL)
            throwreg(temp2[0]).update(memory_content)

        elif throwreg(temp2[0]) == M:
            HL = str(RegPair_Dict["H"])
            dbfuncs.store_value_to_memory(HL, str(throwreg(temp2[1])))
            throwreg("M").update(dbfuncs.retrieve_from_memory(HL))
            dbfuncs.MemoryTransition[HL] = str(throwreg("M"))
        else:
            # throwreg(temp2[0]).updateObj(throwreg(temp2[1]))
            Reg_Dict[temp2[0]].updateObj(Reg_Dict[temp2[1]])

    elif ins == "MVI":
        temp2 = val.split(',')
        checkreg(temp2[0])
        check8bit(temp2[1])
        checkreg8bitvalue(val)
        throwreg(temp2[0]).update(temp2[1])
        if throwreg(temp2[0]) == M:
            HL = str(RegPair_Dict["H"])
            dbfuncs.store_value_to_memory(HL, temp2[1])
            dbfuncs.MemoryTransition[HL] = temp2[1]
            return

    elif ins == "NOP":
        pass

    elif ins == "ORA":
        checkreg(val)
        A = eval('A') | throwreg(val)
        flags.setFlags(A)
        flags.flag['CY'], flags.flag['AC'] = 0, 0

    elif ins == "ORI":
        check8bit(val)
        A = eval('A') | registers(val)
        flags.setFlags(A)
        flags.flag['CY'], flags.flag['AC'] = 0, 0

    elif ins == "OUT":
        check8bit(val)

    elif ins == "PCHL":
        pass

    elif ins == "POP":
        checkregpair(val,["B","D","H","PSW"])
        i = regs.index(throwreg(val))
        if i == 1:
            tmp = eval('BC')
            tmp.update(B, C)
        elif i == 3:
            tmp = eval('DE')
            tmp.update(D, E)
        elif i == 5:
            tmp = eval('HL')
            tmp.update(H, L)
        elif i == 8:
            tmp = eval('PSW')
        tmp.mov(SP.pop())
        if i == 5:
            tmp.dispatch()

    elif ins == "PUSH":
        checkregpair(val, ["B", "D", "H", "PSW"])
        i = regs.index(throwreg(val))
        if i == 1:
            tmp = eval('BC')
            tmp.update(B, C)
        elif i == 3:
            tmp = eval('DE')
            tmp.update(D, E)
        elif i == 5:
            tmp = eval('HL')
            tmp.update(H, L)
        elif i == 8:
            tmp = eval('PSW')
        SP.push(tmp)

    elif ins == "RAL":
        checkNone(val)
        v = eval("A").binary()
        l = str(flags.flag["CY"]) + v
        l = deque(l)
        l.rotate(-1)
        v = list(l)
        flags.flag["CY"] = int(v.pop(0))
        reg = ''.join(v)
        v = int(reg, 2)
        val = hex(v)[2:].upper().zfill(2)
        eval("A").update(val)

    elif ins == "RAR":
        checkNone(val)
        v = eval("A").binary()
        l = v + str(flags.flag["CY"])
        l = deque(l)
        l.rotate(1)
        v = list(l)
        flags.flag["CY"] = int(v.pop())
        reg = ''.join(v)
        v = int(reg, 2)
        val = hex(v)[2:].upper().zfill(2)
        eval("A").update(val)

    elif ins == "RLC":
        checkNone(val)
        v = eval("A").binary()
        flags.flag["CY"] = v[0]
        l = deque(v)
        l.rotate(-1)
        v = list(l)
        reg = ''.join(v)
        v = int(reg, 2)
        val = hex(v)[2:].upper().zfill(2)
        eval("A").update(val)

    elif ins == "RRC":
        checkNone(val)
        v = eval("A").binary()
        l = deque(v)
        l.rotate(1)
        v = list(l)
        reg = ''.join(v)
        flags.flag["CY"] = int(v[0])
        v = int(reg, 2)
        val = hex(v)[2:].upper().zfill(2)
        eval("A").update(val)

    elif ins in ['RET', 'RC', 'RM', 'RNC', 'RPE', 'RP', 'RPO', 'RZ', 'RNZ']:
        checkNone(val)
        if ins == "RNC":
            if flags.flag['CY'] == 0:
                return "return"
            else:
                return "continue"
        if ins == "RMP":
            return "return"
        elif ins == "RC" and flags.flag['CY'] == 1:
            return "return"
        elif ins == "RZ" and flags.flag['Z'] == 1:
            return "return"
        elif ins == "RNZ" and flags.flag['Z'] == 0:
            return "return"
        elif ins == "RP" and flags.flag['S'] == 0:
            return "return"
        elif ins == "RPO" and flags.flag['P'] == 0:
            return "return"
        elif ins == "RM" and flags.flag['S'] == 1:
            return "return"
        elif ins == "RPE" and flags.flag['P'] == 1:
            return "return"
        elif ins == "RET":
            return "return"
        else:
            return "continue"

    elif ins == "RIM":
        checkNone(val)
        pass

    elif ins == "RST":
        if not val in ["0","1","2","3","4","5","6","7"]:
            raise Exception("Restart instruction is not provided with appropriate operand.")

    elif ins == "SBB":
        checkreg(val)
        temp = throwreg(val)
        temp += flags.flag['CY']
        A = eval('A') - temp
        flags.setFlags(A)

    elif ins == "SBI":
        check8bit(val)
        temp = int(val)+int(flags.flag['CY'])
        A = eval('A') - registers(temp)
        flags.setFlags(A)

    elif ins == "SHLD":
        check16bit(val)
        dbfuncs.store_value_to_memory(val, L.reg)
        dbfuncs.MemoryTransition[val] = str(eval("L"))
        val = int(val, 16) + 1
        val = dbfuncs.return_address(val)
        dbfuncs.store_value_to_memory(val, H.reg)
        dbfuncs.MemoryTransition[val] = str(throwreg("H"))

    elif ins == "SIM":
        pass
    elif ins == "SPHL":
        SP.push(eval('HL'))

    elif ins == "STA":
        check16bit(val)
        dbfuncs.store_value_to_memory(val, str(eval("A")))
        dbfuncs.MemoryTransition[val] = str(eval("A"))

    elif ins == "STAX":
        if val == "B":
            dbfuncs.store_value_to_memory(BC.reg, eval('A').reg)
            dbfuncs.MemoryTransition[BC.reg] = str(eval('A'))
        elif val == "D":
            dbfuncs.store_value_to_memory(DE.reg, eval('A').reg)
            dbfuncs.MemoryTransition[DE.reg] = str(eval("A"))
        else:
            raise Exception("Register Pairs B and D are the only ones allowed with STAX instruction.")

    elif ins == "STC":
        checkNone(val)
        flags.flag['CY'] = 1

    elif ins == "SUB":
        checkreg(val)
        A = eval('A') - eval(val)
        flags.setFlags(A)

    elif ins == "SUI":
        check8bit(val)
        A = eval('A') - registers(val)
        flags.setFlags(A)

    elif ins == "XCHG":
        checkNone(val)
        l = [H.reg, L.reg, D.reg, E.reg]
        H.update(l[2])
        L.update(l[3])
        D.update(l[0])
        E.update(l[1])
        eval('HL').dispatch()

    elif ins == "XRA":
        checkreg(val)
        A = eval('A') ^ eval(val)
        flags.setFlags(A)
        flags.flag['CY'], flags.flag['AC'] = 0, 0

    elif ins == "XRI":
        check8bit(val)
        A = eval('A') ^ registers(val)
        flags.setFlags(A)
        flags.flag['CY'], flags.flag['AC'] = 0, 0

    elif ins == "XTHL":
        checkNone(val)
        temporary = eval('HL').reg
        temporary1 = SP.pop()
        HL.reg = temporary
        SP.push(temporary1)

    return
