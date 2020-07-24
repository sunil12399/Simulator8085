import re
from CustomExceptions import *


class LexicalAnalyser:

    def __init__(self):
        self.Stack=[]

    def returnoperands(self,ins):
        zeroOps = ["HLT", "NOP", "RLC", "RAL", "RAR","RIM","DAA","CMA","SIM","STC","CMC","RNZ","RZ","RET","RNC","RC","RPO","XTHL","RPE","PCHL","XCHG","RP","DI","RM","SPHL","EI"]
        oneReg = ["ADD","STAX","INX","INR","DCR", "DCX", "DAD", "ADC", "SUB", "SBB", "ANA", "XRA", "ORA", "CMP", "POP", "PUSH", "LDAX"]
        val = ['ADI','ANI','XRI','SUI','SBI','CPI','IN','OUT','ORI']
        addr4dVal = ["LDA","LHLD","SHLD","STA","JMP"]

        if ins in zeroOps:
            return "ZeroOps"
        elif ins in oneReg:
            return "Reg"
        elif ins == "MOV":
            return "Reg,Reg"
        elif ins == "MVI":
            return "Reg,Val"
        elif ins == "LXI":
            return "Reg,4dVal"
        elif ins in addr4dVal:
            return "Address"
        elif ins in val:
            return "Val"
        elif ins in ['CALL', 'CC', 'CM', 'CNC', 'CP', 'CPE', 'CPO', 'CZ', 'CNZ', 'JC', 'JM', 'JMP', 'JNC', 'JNZ', 'JP', 'JPE', 'JPO', 'JZ']:
            return "Label"
        else:
            return 0

    def analyse(self, other):
        self.Stack = []
        """
        This function analyses the input program for syntactical errors and Lexical errors if any and raises exception
        which is handled by the Main program. It then parses the input code to the instructionInterpret() in SimMain.MainProg
        """
        code = other.textEdit.toPlainText()

        labels = re.findall(r'[\w]+:', code)
        Uniquelabels = list(dict.fromkeys(labels))
        if len(labels) != len(Uniquelabels):
            raise Exception("Names for the Labels must be unique.")

        # remove trailing empty lines from the code
        text = code.strip("\n")

        text = re.split("\n", text.upper())
        try:
            text = [text.remove('') for i in range(len(text))]
        except ValueError:
            # Meaning that the list has no further '' which is why it throws a ValueError exception in remove()
            pass

        # remove full comment lines
        for i in range(0, len(text)):
            text[i] = text[i].strip(" ")
            index = text[i].find(';')
            # if a sentence has ';' then words following it is a comment remove it
            # by only taking the words preceding it
            if index != -1:
                text[i] = text[i][:index]

        # remove other things or raise errors
        for index, txt in enumerate(text):
            # remove H representing hexadecimal values from 8-bit and 16-bit values
            # for e.g 90 H or 90AB H
            txt = txt.strip(" ")
            if re.search(r'[0-9a-hA-H][0-9A-Ha-h][ ]*[H]?$', txt):
                if txt.endswith("H"):
                    if not re.search(r'DAD|ADD|ADC H', txt):
                        text[index] = txt.rstrip("H")

            # Split the instruction into its components
            txt = re.split("\s", text[index])

            # now all spaces will look like '' in the list e.g list =[mvi,'','','',...]
            # now removing duplicates by converting list to a dictionary then again to a list
            txt = list(dict.fromkeys(txt))
            # still one '' may be left
            if '' in txt:
                txt.remove('')
            try:
                if ':' in txt:
                    pos = txt.index(':')
                    if pos == 0:
                        raise LexicalException("Misplaced \':\'")
                    if self.returnoperands(txt[pos-1]) == 0:
                        txt[pos-1] = txt.pop(pos-1) + ":"
            except ValueError:
                pass
            except IndexError:
                other.WarningLabel.setText("Something doesn't looks alright at line "+ str(index+1))

            try:
                if ',' in txt:
                    pos = txt.index(',')
                    if pos == 0:
                        raise LexicalException("Misplaced \",\"")
                    if self.returnoperands(txt[pos-1]) == 0 and txt[pos-1] in ['A', 'B', 'C', 'D', 'E', 'H', 'L', 'M', 'SP', 'PC', 'PSW']:
                        txt[pos-1] = txt.pop(pos-1) + "," + txt.pop(pos)
            except ValueError:
                pass
            except IndexError:
                other.WarningLabel.setText("Something doesn't looks alright at line "+ str(index+1))

            for num,words in enumerate(txt):
                if words.endswith(':') and words != ":":
                    # if a word itself endswith : then it must e a label and hence no operation is required
                    continue
                if words.endswith(',') and words != ",":
                    try:
                        if words[:-1] in ['A', 'B', 'C', 'D', 'E', 'H', 'L', 'M', 'SP', 'PC', 'PSW']:
                            txt[num] = txt.pop(num) + txt[num]
                            num += 1
                    except IndexError:
                        other.WarningLabel.setText("something doesn't seems right at line "+str(index+1))
            self.Stack.append(txt)

        return self.Stack