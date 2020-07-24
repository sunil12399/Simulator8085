import sqlite3
from sqlite3 import Error
from Main.classcode import main as obj
import os.path

MemoryTransition = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Compiler.db")


def return_instructions(ins):
    instruction = {
             'M': ['MOV', 'MVI'],
             'A': ['ADI', 'ACI', 'ADD', 'ANA', 'ANI', 'ADC'],
             'C': ['CALL', 'CC', 'CM', 'CMA', 'CMC', 'CMP', 'CNC', 'CP', 'CPE', 'CPI', 'CPO', 'CZ', 'CNZ'],
             'D': ['DAA', 'DAD', 'DCR', 'DCX', 'DI'],
             'E': ['EI'],
             'H': ['HLT'],
             'I': ['IN', 'INX', 'INR'],
             'J': ['JC', 'JM', 'JMP', 'JNC', 'JNZ', 'JP', 'JPE', 'JPO', 'JZ'],
             'L': ['LDA', 'LDAX', 'LHLD', 'LXI'],
             'N': ['NOP'],
             'O': ['ORA', 'ORI', 'OUT'],
             'P': ['PCHL', 'POP', 'PUSH'],
             'R': ['RAR', 'RRC', 'RAL', 'RLC', 'RET', 'RC', 'RIM', 'RM', 'RNC', 'RPE', 'RP', 'RPO', 'RST', 'RZ', 'RNZ'],
             'S': ['SBB', 'SUB', 'SUI', 'SHLD', 'SIM', 'SPHL', 'STA', 'STAX', 'STC', 'SBI'],
             'X': ['XCHG', 'XRA', 'XRI', 'XTHL']
            }

    try:
        for i in instruction.get(ins[0]):
            if ins == i:
                return ins
    except TypeError:
        raise Exception(ins + " is not an instruction.")
    finally:
        pass
    return 0


def return_address(num, mstart="0000"):
    num = num + int(mstart, 16)
    address_variable = hex(num)[2:].upper()
    return address_variable.zfill(4)


# def retOpcode(connection,table,instruction,reg):
#     connection=sqlite3.connect(db_path)
#     c=connection.cursor()
#     query="SELECT Opcode FROM MemHex WHERE Instruction=instruction and Reg=reg"
#     result=c.execute(query)
#     connection.close()


def storeInsMemOpcode(row, label, mnemonics, ins, var=''):
    address_variable = ''
    connection = sqlite3.connect(db_path)
    c = connection.cursor()
    c.execute("select opcode from MemHex where Instruction=? and reg=?", (ins, var))
    result = c.fetchone()
    try:
        address_variable = return_address(row)
        c.execute("INSERT INTO MemOpcode VALUES(?,?,?,?,?)", (row, address_variable, label, mnemonics, result[0]))

    except Error as e:
        """ remove the row if already present and then insert thee new updated row"""
        c.execute("DELETE FROM MemOpcode where AddrId = (?)", (row))
        c.execute("INSERT INTO MemOpcode VALUES(?,?,?,?,?)", (row, address_variable, label, mnemonics, result[0]))
    finally:
        obj.RegisterPairs[0] = return_address(row+1)
        connection.commit()
        connection.close()
    return row+1


def storeValMemOpcode(row, val):
    address_variable = ''
    connection = sqlite3.connect(db_path)
    c = connection.cursor()
    try:
        address_variable = return_address(row)
        if len(val) == 4:
            try:
                c.execute("INSERT INTO MemOpcode VALUES(?,?,?,?,?)", (row, address_variable, '', '', str(val[2:4])))
            except:
                c.execute("DELETE FROM MemOpcode where AddrId = (?)", str(row))
                c.execute("INSERT INTO MemOpcode VALUES(?,?,?,?,?)", (row, address_variable, '', '', str(val[2:4])))
            row += 1
            obj.RegisterPairs[0] = return_address(row+1)
            try:
                address_variable = return_address(row)
                c.execute("INSERT INTO MemOpcode VALUES(?,?,?,?,?)", (row, address_variable, '', '', str(val[:2])))
            except:
                c.execute("DELETE FROM MemOpcode where AddrId = (?)", str(row))
                c.execute("INSERT INTO MemOpcode VALUES(?,?,?,?,?)", (row, address_variable, '', '', str(val[:2])))
            obj.RegisterPairs[0] = return_address(row+1)
        elif len(val) == 2:
            try:
                c.execute("INSERT INTO MemOpcode VALUES(?,?,?,?,?)", (row, address_variable, '', '', str(val)))
            except:
                c.execute("DELETE FROM MemOpcode where AddrId = (?)", str(row))
                c.execute("INSERT INTO MemOpcode VALUES(?,?,?,?,?)", (row, address_variable, '', '', str(val)))
            obj.RegisterPairs[0] = return_address(row+1)
    finally:
        connection.commit()
        connection.close()
    return row + 1


def retrieve_from_memory(memory_address):
    """

    @rtype: object
    """
    connection = sqlite3.connect(db_path)
    c = connection.cursor()
    result = ''
    try:
        c.execute('select opcode from MemOpcode where Address = ?', (memory_address,))
        result = c.fetchone()
        return result[0]
    except TypeError as e:
        if result is None:
            return "00"
    except Error as e:
        print("in db.py" + str(e))
    finally:
        connection.commit()
        connection.close()


def store_value_to_memory(memory_address, value):
    connection = sqlite3.connect(db_path)
    c = connection.cursor()
    try:
        c.execute("INSERT INTO MemOpcode VALUES(?,?,?,?,?)", (int(memory_address, 16), memory_address, '', '', value))
    except Error as e:
        c.execute("update MemOpcode set opcode=? where Address=(?)", (value, memory_address))
    finally:
        connection.commit()
        connection.close()
    return


def destroy():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("delete from MemOpcode")
    conn.commit()
    conn.close()


def loadData(rowno, num):
    connection = sqlite3.connect(db_path)
    c = connection.cursor()
    for i in range(0,rowno+num):
        address_variable = return_address(i)
        try:
            c.execute("INSERT INTO MemOpcode VALUES(?,?,?,?,?)", (i, address_variable, '', '', ''))
        except:
            print("DataBase Error!!!")
    connection.commit()
    connection.close()


def results():
    connection = sqlite3.connect(db_path)
    query = "SELECT Address, Label, Mnemonics, opcode FROM MemOpcode"
    result = connection.execute(query)
    return (result, connection)