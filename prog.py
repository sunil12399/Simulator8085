from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QAction, QMessageBox, QSplashScreen
from Main.Gui import LatestUI
from Main.Database import Db as dbfuncs
from Main.classcode import main as obj
# from Main.Objects import RegObject as obj
from Main.Objects import flags
from Main.SimMain import MainProg as func
from Highlighter import *
from Validate import *
from CustomExceptions import *
from ioeditordialog import Ui_IOEditor

from MemoryEditor import Ui_AddressEditor
from Exit import Ui_ExitDialog
import time

sw = False
afunc = False
execute = False
assemble = False


class UI_Edit(LatestUI.Ui_MainWindow):
    def __init__(self):
        LatestUI.Ui_MainWindow.__init__(self)
        self.rowno = 0
        self.steps_counter = 0
        self.UpdatedRow = 0
        self.Stack = []
        # to copy Stack with label and mnemonics
        self.stack =[]
        # flow counter = {label : row no}
        self.FlowCounter = {}
        self.LastCall = []
        # label mapper = { label : (instruction no, Memory address)}
        self.LabelMapper = {}
        # Memory mapper = { rowno : memory}
        self.MemoryMapper = {}

        self.IOMapper = {}
        self.lanalyser = LexicalAnalyser()
        obj.PC.updateFromString(self.MemoryStartAddress)
        obj.SP.updateFromString(self.StackPointerAddress)
        # Assembled is a flag that denotes whether the program is assembled. It is useful for buttons on the Assembled
        # tab. So that they are only used if the code is assmbled.
        self.Assembled = 0
        self.CancelledSave = True

    def updateAddresses(self):
        obj.PC.updateFromString(self.MemoryStartAddress)
        obj.SP.updateFromString(self.StackPointerAddress)
        self.showRegisterContents()

    def do_something(self):
        try:
            if self.textEdit.toPlainText() == '':
                raise Exception("Please Enter 8085 code in order to get output.")
        except Exception as e:
            self.WarningLabel.setText(str(e))
            return

        self.showOutput()
        self.Assembled = 1

    def hexCodeMapper(self,temp):
        i, length = 0, len(temp)
        self.UpdatedRow = int(self.MemoryStartAddress, 16)
        # label = lambda row: [keys if FC[keys] else '' for keys in FC.keys() if FC[keys] == row]
        try:
            while i < length:
                if len(temp[i]) == 0:
                    # if a blank line is encountered then continue by proceeding to next row
                    i += 1
                    continue
                if temp[i][0] == dbfuncs.return_instructions(temp[i][0]):
                    v = self.returnoperands(temp[i][0])

                    if v == "ZeroOps" or v == "Returns":
                        self.MemoryMapper[i] = dbfuncs.return_address(self.UpdatedRow)
                        self.UpdatedRow = dbfuncs.storeInsMemOpcode(self.UpdatedRow, self.stack[i][0], self.stack[i][1],
                                                                    temp[i][0])

                    elif v == "Reg,Reg" or v == "Reg":
                        self.MemoryMapper[i] = dbfuncs.return_address(self.UpdatedRow)
                        self.UpdatedRow = dbfuncs.storeInsMemOpcode(self.UpdatedRow, self.stack[i][0], self.stack[i][1], temp[i][0], temp[i][1])

                    elif v == "Reg,Val" or v == "Reg,4dVal":
                        tempo = re.split(',', temp[i][1])
                        self.MemoryMapper[i] = dbfuncs.return_address(self.UpdatedRow)
                        self.UpdatedRow = dbfuncs.storeInsMemOpcode(self.UpdatedRow, self.stack[i][0], self.stack[i][1], temp[i][0],tempo[0])
                        self.UpdatedRow = dbfuncs.storeValMemOpcode(self.UpdatedRow,tempo[1])

                    elif v == "Val" or v == "Address":
                        self.MemoryMapper[i] = dbfuncs.return_address(self.UpdatedRow)
                        self.UpdatedRow = dbfuncs.storeInsMemOpcode(self.UpdatedRow, self.stack[i][0],  self.stack[i][1],temp[i][0])
                        self.UpdatedRow = dbfuncs.storeValMemOpcode(self.UpdatedRow, temp[i][1])

                    elif v == "Label":
                        self.MemoryMapper[i] = dbfuncs.return_address(self.UpdatedRow)
                        self.UpdatedRow = dbfuncs.storeInsMemOpcode(self.UpdatedRow,  self.stack[i][0],  self.stack[i][1], temp[i][0])
                        checker = temp[i][1]+':'
                        res = self.LabelMapper[checker]
                        if res:
                            self.UpdatedRow = dbfuncs.storeValMemOpcode(self.UpdatedRow, res[1])
                        else:
                            self.WarningLabel.setText("Label does not exist")
                else:
                    self.WarningLabel.setText("Warning: " + str(temp[i][0]) + " Instruction does not exist. "
                                                                              "Error occurred at line " + str(i))
                    return
                i += 1
        except Exception as e:
            self.WarningLabel.setText("Warning: "+str(e))
        self.steps_counter = 0

    def interpreter(self):
        try:
            if self.textEdit.toPlainText() == '':
                raise Exception("Please Enter 8085 code in order to get output.")
            self.Stack = self.lanalyser.analyse(self)

        except LexicalException as e:
            self.WarningLabel.setText(str(e))
        except Exception as e:
            self.WarningLabel.setText(str(e))
            return

        length = len(self.Stack)
        i = 0
        for j in range(0, length):
            if re.search(r'[\w]+:$', self.Stack[j][0]):
                if len(self.Stack[j]) == 1:
                    i+=1
                self.FlowCounter[self.Stack[j][0]] = i
                self.Stack[j].pop(0)
            i += 1

        """ We have stripped the labels from the 'Stack'. But in order to display the output we have to show the labels.
            Hence we use 'stack' another data structure where we join and append labels from self.label(row) and 
            label-stripped-instructions from the 'Stack'.        
         """
        for i,j in enumerate(self.Stack):
            temporal = (self.label(i),' '.join(j))
            self.stack.append(list(temporal))

        """
        for Program Counter and stack Pointer remove self.MemoryMapper[i] = dbfuncs.return_address(self.UpdatedRow) line
        from hexCodeMapper() and use the lastMemoryRow instead to fill the self.MemoryMapper 
        """
        # MemoryRow is row_id of Memory. return_rows() returns no of row instruction will use
        MemoryRow = 0
        for ins_no, instruction in enumerate(self.Stack):
            if len(instruction) == 0:
                MemoryRow += 1
                continue
            lastMemoryRow = MemoryRow
            rows = self.return_rows(instruction[0])
            MemoryRow += rows
            if ins_no in self.FlowCounter.values():
                try:
                    addr = dbfuncs.return_address(lastMemoryRow, self.MemoryStartAddress)
                except:
                    self.WarningLabel.setText("Warning: An error has Occurred. Please rerun the application.")
                label = self.label(ins_no)
                self.LabelMapper[label] = (ins_no, addr)
        return

    def MainFunc(self):
        temp = self.Stack
        length, i = len(temp), 0
        try:
            while i < length:
                if len(temp[i]) == 0:
                    # if a blank line is encountered then continue
                    i += 1
                    continue
                # df = deciding factor
                # check what an instruction returns if it is a 1 byte instruction for e.g hlt
                df = self.returnoperands(temp[i][0])
                if df == 0:
                    raise Exception(temp[i][0] + " is not an instruction.")
                if df == "ZeroOps":
                    func.instructonInterpret(temp[i][0])
                    i += 1
                    continue

                if temp[i][0] == 'IN':
                    func.instructonInterpret(temp[i][0],temp[i][1])
                    try:
                        obj.throwreg('A').update(self.IOMapper[temp[i][1]])
                    except KeyError:
                        obj.throwreg('A').update("00")
                    i += 1
                    continue

                elif temp[i][0] == "OUT":
                    func.instructonInterpret(temp[i][0], temp[i][1])
                    self.IOMapper[temp[i][1]] = str(obj.throwreg('A'))
                    i += 1
                    continue

                if temp[i][0] in ['JC', 'JM', 'JMP', 'JNC', 'JNZ', 'JP', 'JPE', 'JPO', 'JZ']:
                    determinant_var = func.instructonInterpret(temp[i][0])
                    if determinant_var == "iterate":
                        check_variable = temp[i][1]+':'
                        TargetRow = self.FlowCounter.get(check_variable)
                        if TargetRow is None:
                            del TargetRow
                            raise Exception("Label \"" +temp[i][1] +"\" is not specified earlier.")
                        else:
                            i = TargetRow
                        continue
                    i += 1
                    continue

                if temp[i][0] in ['CALL', 'CC', 'CM', 'CNC', 'CP', 'CPE', 'CPO', 'CZ', 'CNZ']:
                    determinant_var = func.instructonInterpret(temp[i][0])
                    if determinant_var == "goto":
                        address = self.MemoryMapper[i+1]
                        obj.SP.push(address)
                        self.LastCall.append(i)  # LastCall may be needed as a list
                        check_variable = temp[i][1]+':'
                        TargetRow = self.FlowCounter.get(check_variable)
                        if TargetRow is None:
                            del TargetRow
                            raise Exception("Label \"" +temp[i][1] +"\" is not specified earlier.")
                        else:
                            i = TargetRow
                        continue
                    i += 1
                    continue

                if df == "Returns":
                    determinant_var = func.instructonInterpret(temp[i][0])
                    if determinant_var == "return":
                        obj.SP.pop()
                        i = self.LastCall.pop(0) + 1
                        continue
                    i += 1
                    continue

                # if it is a simple instruction and operand
                func.instructonInterpret(temp[i][0], temp[i][1])
                i += 1
        except RegisterError:
            self.WarningLabel.setText(temp[i][0] + " does not have a valid register at line " + str(i + 1))
            return
        except Hexadecimal8bitValueError as e:
            self.WarningLabel.setText(temp[i][0] + " does not have a valid 8-bit hexadecimal value. "
                                                   "Error occurred at line " + str(i + 1))
            return
        except Hexadecimal16bitValueError as e:
            self.WarningLabel.setText(temp[i][0] + " does not have a valid 16-bit hexadecimal value."
                                                   " Error occurred at line " + str(i + 1))
            return
        except NotNoneError:
            self.WarningLabel.setText(temp[i][0] + " is supposed to have no operands. Error occurred at line " + str(i + 1))
            return
        except EndException:
            return
        except Exception as e:
            self.WarningLabel.setText(str(e) + " Error occurred at line " + str(i + 1))
        finally:
            self.showRegisterContents()
            self.showFlagContents()
            self.set_memory_widget()
            return

    def setupUiWithVals(self):
        ypos = 0
        for i in obj.regs:
            self.RegisterContentWidget.setItem(ypos,1, QTableWidgetItem(i.reg))
            ypos += 1

        ypos = 0
        for i in obj.RegisterPairs:
            self.tableWidget.setItem(ypos, 1, QTableWidgetItem(i.reg))
            ypos += 1

        xpos = 0
        for j in flags.flag:
            self.FlagContentWidget.setItem(0,xpos, QTableWidgetItem(str(flags.flag[j])))
            xpos += 1

        def resetStep():
            self.steps_counter = 0
            self.MemHexTable.selectRow(0)
        resetStep()

        # Actions
        resetSteps = QAction("Reset Steps", self)
        resetSteps.setStatusTip("Reset Step Execution to instruction 1")
        resetSteps.triggered.connect(resetStep)

        showIOAction = QAction("I/O Editor", self)
        showIOAction.triggered.connect(self.showIOEditor)

        editMemory = QAction("Edit Memory and Stack", self)
        editMemory.setStatusTip("Edit Start Addresses of memory and stack")
        editMemory.triggered.connect(self.showMemoryEditor)

        resetDataStructures = QAction("Reset ALL", self)
        resetDataStructures.setStatusTip("Reset the registers, memory, flags to the default value.")
        resetDataStructures.triggered.connect(self.totalReset)

        openHelp = QAction(QIcon("icons/help.png"),"Mnemonics", self)
        openHelp.setStatusTip("Get Help on 8085 Mnemonics.")
        openHelp.triggered.connect(self.viewHelp)

        help = QAction(QIcon("icons/help.png"),"Getting Started", self)
        help.setStatusTip("Get Help on Using the Simulator.")
        help.triggered.connect(self.viewSimulatorBasics)

        openAbout = QAction(QIcon("icons/help.png"),"About", self)
        openAbout.triggered.connect(self.showAbout)

        self.settings.addAction(editMemory)
        self.tools.addAction(showIOAction)
        self.tools.addAction(resetDataStructures)
        self.tools.addAction(resetSteps)
        self.toolbar.addAction(resetDataStructures)
        self.toolbar.addAction(resetSteps)

        self.HelpMenu = self.menubar.addMenu("Help")
        self.HelpMenu.addAction(help)
        self.HelpMenu.addAction(openHelp)
        self.HelpMenu.addAction(openAbout)

        self.tabWidget.setCurrentIndex(0)
        dbfuncs.destroy()
        dbfuncs.loadData(self.rowno,20)
        self.connectTable()
        self.rowno += 20

    def showAbout(self):
        about = """
        <html>
        <head/>
        <body>
        <p style="font-size: 11pt; margin-left: 3em">
        <br>
        Version 1.0<br>
        Developed by Sunil A. Bahelia<br>
        Licensed under the GNU Public License.
        </p>
        </body>
        </html> 
        """
        title = "<p style = \"padding-right: 5em; font-size: 15pt; font-weight:500\">Simulator for the 8085 Microprocessor</p>"
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("About")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(title)
        msgBox.setInformativeText(about)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def viewSimulatorBasics(self):
        pass

    def viewHelp(self):
        self.centralwidget.setEnabled(False)
        import webbrowser
        import os
        # Change path to reflect file location
        filename = 'file:///' + os.getcwd() + '/Help/' + 'csstest.html'
        webbrowser.open_new_tab(filename)
        self.centralwidget.setEnabled(True)

    def totalReset(self):
        self.steps_counter = 0
        flags.flag = {
            'S': 0,
            'Z': 0,
            'D5': 0,
            'AC': 0,
            'D3': 0,
            'P': 0,
            'D1': 0,
            'CY': 0
        }
        obj.A.update("00")
        obj.B.update("00")
        obj.C.update("00")
        obj.D.update("00")
        obj.E.update("00")
        obj.H.update("00")
        obj.L.update("00")
        obj.M.update("00")

        obj.PSW.updatePSW(obj.A, flags.flag)
        obj.BC.update(obj.B, obj.C)
        obj.DE.update(obj.D, obj.E)
        obj.HL.update(obj.H, obj.L)
        obj.SP.updateFromString(self.StackPointerAddress)
        obj.PC.updateFromString(self.MemoryStartAddress)

        dbfuncs.destroy()
        self.clear()
        self.textEdit.clear()
        self.MemHexTable.setRowCount(30)
        self.connectTable()
        self.showRegisterContents()
        self.showFlagContents()

    def showOutput(self):
        self.tabWidget.setCurrentIndex(1)
        self.connectTable()

    def showRegisterContents(self):
        regs = obj.regs
        for i,j in enumerate(regs):
            self.RegisterContentWidget.setItem(i, 1, QTableWidgetItem(str(j)))

        registerpairs = obj.RegisterPairs
        for i, j in enumerate(registerpairs):
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(j)))
        return

    def showFlagContents(self):
        flag = flags.flag
        for i, j in enumerate(flag):
            self.FlagContentWidget.setItem(0, i, QTableWidgetItem(str(flag[j])))
        return

    def set_memory_widget(self):
        memory = dbfuncs.MemoryTransition
        for a,b in enumerate(memory):
            self.Memory_Widget.setItem(a, 0, QTableWidgetItem(b))
            self.Memory_Widget.setItem(a, 1, QTableWidgetItem(memory[b]))
        return

    @staticmethod
    def returnoperands(ins):
        zeroOps = ["HLT", "NOP", "RLC", "RRC", "RAL", "RAR","RIM","DAA","CMA","SIM","STC","CMC","XTHL","PCHL","XCHG","DI","SPHL","EI"]
        oneReg = ["ADD","STAX","INX","INR","DCR", "DCX", "DAD", "ADC", "SUB", "SBB", "ANA", "XRA", "ORA", "CMP", "POP", "PUSH", "LDAX"]
        val = ['ADI','ANI','XRI','SUI','SBI','CPI','IN','OUT','ORI']
        addr4dVal = ["LDA","LHLD","SHLD","STA"]

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
        elif ins in ['RET', 'RC', 'RM', 'RNC', 'RPE', 'RP', 'RPO', 'RZ', 'RNZ']:
            return "Returns"
        else:
            return 0

    def return_rows(self, ins):
        if ins == "LXI":
            return 3
        res = self.returnoperands(ins)
        if res == "ZeroOps" or res == "Reg" or res == "Reg,Reg":
            return 1
        elif res == "Reg,Val" or res == "Val":
            return 2
        elif res == "Address" or "Label":
            return 3
        else:
            return 0

    def label(self, row):
        for keys in self.FlowCounter.keys():
            if self.FlowCounter[keys] == row:
                return keys
        else:
            return ''

    def connectTable(self):
        self.MemHexTable.setRowCount(0)
        result = dbfuncs.results()
        for row_no, data in enumerate(result[0]):
            self.MemHexTable.insertRow(row_no)
            for col_no, data in enumerate(data):
                self.MemHexTable.setItem(row_no, col_no, QTableWidgetItem(str(data)))
        result[1].close()
        return

    def get_from_memory_widget(self):

        """ The get_from_memory_widget() function accepts the value from the Memory_Widget and deals with any or all
            unexpected inputs that may be encountered b the exception.
        """
        self.WarningLabel.setText("")
        set_empty = lambda item: item.text().upper() if item else ''
        temp_memory = {}
        num_rows = self.Memory_Widget.rowCount()
        try:
            for row in range(num_rows):
                address = self.Memory_Widget.item(row, 0)
                address = set_empty(address)
                hex_value = self.Memory_Widget.item(row, 1)
                hex_value = set_empty(hex_value)
                if address != '' or hex_value != '':
                    if address == '':
                        raise Hexadecimal16bitValueError("Enter the corresponding Address")
                    if hex_value == '':
                        raise Hexadecimal8bitValueError("Enter the corresponding Value")
                    func.check8bit(hex_value)
                    func.check16bit(address)
                    temp_memory[address] = hex_value
            del temp_memory['']

        except KeyError:
            pass
        except Hexadecimal8bitValueError as e:
            self.WarningLabel.setText(str(e) + " in Memory Table")
            return
        except Hexadecimal16bitValueError as e:
            self.WarningLabel.setText(str(e) + " in Memory Table")
            return

        dbfuncs.MemoryTransition = temp_memory

        for address, value in temp_memory.items():
            dbfuncs.store_value_to_memory(address, value)

    def step_execution(self):
        try:
            if self.textEdit.toPlainText() == '':
                raise Exception("Please Enter 8085 code in order to get output.")
            if self.Assembled == 0:
                raise Exception("Please Assemble the code before using Step Exceution")
            self.get_from_memory_widget()
        except Exception as e:
            self.WarningLabel.setText(str(e))
            return

        df = ''
        temp = self.Stack
        i = self.steps_counter
        if len(temp[i]) == 0:
            # if a blank line is encountered then continue
            # self.steps_counter += 1
            i += 1
        try:
            # df = deciding factor
            # It checks what an instruction returns if it is a 1 byte instruction for e.g hlt
            df = self.returnoperands(temp[i][0])
        except IndexError:
            i, self.steps_counter = 0, 0

        if df == "Returns":
            determinant_var = func.instructonInterpret(temp[i][0])
            if determinant_var == "return":
                obj.SP.pop()
                try:
                    self.steps_counter = self.LastCall.pop(0) + 1
                except IndexError:
                    self.status.showMessage("Reached End of Subroutine")
                return
            self.steps_counter += 1
            return

        if temp[i][0] == 'IN':
            func.instructonInterpret(temp[i][0], temp[i][1])
            try:
                obj.throwreg('A').update(self.IOMapper[temp[i][1]])
            except KeyError:
                obj.throwreg('A').update("00")
            self.steps_counter += 1
            return

        elif temp[i][0] == "OUT":
            func.instructonInterpret(temp[i][0], temp[i][1])
            self.IOMapper[temp[i][1]] = str(obj.throwreg('A'))
            self.steps_counter += 1
            return

        if temp[i][0] in ['JC', 'JM', 'JMP', 'JNC', 'JNZ', 'JP', 'JPE', 'JPO', 'JZ']:
            determinant_var = func.instructonInterpret(temp[i][0])
            if determinant_var == "iterate":
                check_variable = temp[i][1] + ':'
                self.steps_counter = self.FlowCounter.get(check_variable)
                if self.steps_counter is None:
                    self.steps_counter = 0
                    self.MemHexTable.selectRow(0)
                    raise Exception("Label is not specified earlier.")
                return
            self.steps_counter += 1
            # print(self.steps_counter,"  ", end='')
            return

        if temp[i][0] in ['CALL', 'CC', 'CM', 'CNC', 'CP', 'CPE', 'CPO', 'CZ', 'CNZ']:
            determinant_var = func.instructonInterpret(temp[i][0])
            if determinant_var == "goto":
                address = self.MemoryMapper[i + 1]
                obj.SP.push(address)
                self.LastCall.append(i)  # LastCall may be needed as a list
                check_variable = temp[i][1] + ':'
                TargetRow = self.FlowCounter.get(check_variable)
                if TargetRow is None:
                    del TargetRow
                    raise Exception("Label is not specified earlier.")
                else:
                    self.steps_counter = TargetRow
                return
            self.steps_counter += 1
            return
        try:
            # if it is a 1 byte instruction
            if df == "ZeroOps":
                func.instructonInterpret(temp[i][0])
                self.steps_counter += 1
                return
            # if it is a simple instruction and operand
            func.instructonInterpret(temp[i][0], temp[i][1])
        except EndException as e:
            self.status.showMessage(str(e))
            self.steps_counter = -1

        self.steps_counter += 1
        self.showRegisterContents()
        self.showFlagContents()
        self.connectTable()
        self.set_memory_widget()

    def highlightrow(self):
        """
        It highlights the row that is being executed at the time while executing one instruction at a time
        """
        try:
            var = int(self.MemoryMapper[self.steps_counter], 16)
            var = var - int(self.MemoryStartAddress, 16)
            # print(var)
            self.MemHexTable.selectRow(var)

        except KeyError:
            self.MemHexTable.selectRow(0)

    def NullCheck(self):
        try:
            if self.textEdit.toPlainText() == '':
                raise Exception("Please Enter 8085 code in order to get output.")
            self.get_from_memory_widget()
        except Exception as e:
            self.WarningLabel.setText(str(e))
            return

    def resetDS(self):
        self.MemoryMapper = {}
        self.stack, self.Stack = [], []
        self.FlowCounter = {}

    def showIOEditor(self):
        ui = Ui_IOEditor(self)
        ui.show()
        ui.exec_()

    def showMemoryEditor(self):
        ui = Ui_AddressEditor(self)
        ui.show()
        ui.exec_()

    def disable(self):
        self.centralwidget.setEnabled(False)

    def closeEvent(self, event):
        if self.Saved:
            reply = QMessageBox.question(self, 'Close Application', 'Are you sure you want to close the application?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            try:
                ui = Ui_ExitDialog(self)
                ui.show()
                ui.exec_()
            except SystemExit:
                self.close()
            if not self.CancelledSave:
                event.accept()
            else:
                event.ignore()

    def initialProcess(self):
        self.Saved = False

    def buttonClicked(self):
        sender = self.sender()
        self.disable()
        if sender.text() == "Run Whole":
            self.get_from_memory_widget()
            self.MainFunc()

        if sender.text() == "Execute":
            self.resetDS()
            dbfuncs.destroy()
            self.NullCheck()
            self.interpreter()
            self.hexCodeMapper(self.Stack)
            self.get_from_memory_widget()
            self.MainFunc()

        if sender.text() == "Assemble":
            self.resetDS()
            dbfuncs.destroy()
            self.NullCheck()
            self.interpreter()
            self.hexCodeMapper(self.Stack)
            self.do_something()

    def take(self):
        try:
            self.textEdit.editingFinished.connect(self.initialProcess)
            self.ExecuteButton.clicked.connect(self.buttonClicked)
            self.AssembleButton.clicked.connect(self.buttonClicked)
            self.RunAllBtn.clicked.connect(self.buttonClicked)

            self.StepExecBtn.clicked.connect(self.disable)
            self.StepExecBtn.clicked.connect(self.step_execution)
            self.StepExecBtn.clicked.connect(self.highlightrow)

            self.connectTable()

        except Exception:
            self.WarningLabel.setText("Warning: An error has Occurred. Please rerun the application.")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    # Create and display the splash screen
    splash_pix = QPixmap('icons/Simulator_Logo.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    # Simulate something that takes time
    # time.sleep(2)

    ui = UI_Edit()
    ui.setupUiWithVals()

    hl = Highlighter(ui.textEdit.document())
    ui.textEdit.show()
    ui.take()
    ui.show()
    dbfuncs.destroy()

    splash.finish(ui)
    app.exec_()
    sys.exit(0)