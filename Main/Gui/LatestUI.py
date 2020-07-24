import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrintDialog, QPrinter
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from NumberConverter import *

var = 0
f = ""
choiceStr = ""
cs = False
wwo = False

tt = True
tf = True
ts = True


class Find(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        self.initUI()

    def initUI(self):

        self.lb1 = QLabel("Search for: ", self)
        self.lb1.setStyleSheet("font-size: 15px; ")
        self.lb1.move(10, 10)

        self.te = QTextEdit(self)
        self.te.move(10, 40)
        self.te.resize(250, 25)

        self.src = QPushButton("Find", self)
        self.src.move(270, 40)

        self.lb2 = QLabel("Replace all by: ", self)
        self.lb2.setStyleSheet("font-size: 15px; ")
        self.lb2.move(10, 80)

        self.rp = QTextEdit(self)
        self.rp.move(10, 110)
        self.rp.resize(250, 25)

        self.rpb = QPushButton("Replace", self)
        self.rpb.move(270, 110)

        self.opt1 = QCheckBox("Case sensitive", self)
        self.opt1.move(10, 160)
        self.opt1.stateChanged.connect(self.CS)

        self.opt2 = QCheckBox("Whole words only", self)
        self.opt2.move(10, 190)
        self.opt2.stateChanged.connect(self.WWO)

        self.close = QPushButton("Close", self)
        self.close.move(270, 220)
        self.close.clicked.connect(self.Close)

        self.setGeometry(300, 300, 360, 250)

    def CS(self, state):
        global cs

        if state == QtCore.Qt.Checked:
            cs = True
        else:
            cs = False

    def WWO(self, state):
        global wwo
        print(wwo)

        if state == QtCore.Qt.Checked:
            wwo = True
        else:
            wwo = False

    def Close(self):
        self.hide()


class MyTextEdit(QTextEdit):
    editingFinished = QtCore.pyqtSignal()
    receivedFocus = QtCore.pyqtSignal()

    def __init__(self, parent):
        super(MyTextEdit, self).__init__(parent)
        self._changed = False
        self._SomeWorked = False
        self._Assembled = False
        self.setTabChangesFocus(True)
        self.textChanged.connect(self._handle_text_changed)

    def focusInEvent(self, QFocusEvent):
        super(MyTextEdit, self).focusInEvent(QFocusEvent)
        self.receivedFocus.emit()

    def focusOutEvent(self, QFocusEvent):
        if self._changed:
            self.editingFinished.emit()
        super(MyTextEdit, self).focusOutEvent(QFocusEvent)

    def _handle_text_changed(self):
        self._changed = True
        self._Assembled = False
        self._SomeWorked = False

    def setTextChanged(self, state = True):
        self._changed = state


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self, None)
        self.MemoryStartAddress = "0000"
        self.StackPointerAddress = "FFFF"
        self.Saved = True
        self.CancelledSave = True
        self.initUI()

    def openNumberConverter(self):
        ui = Ui_NumberConverter()
        ui.show()
        ui.exec_()

    def handleToggleTool(self):
        global tt

        if tt:
            self.toolbar.hide()
            tt = False
            if tf:
                self.HomePage.move(0, 60)
                self.resize(883, 745)
            else:
                self.HomePage.move(0, 30)
                self.resize(883, 730)
        else:
            self.toolbar.show()
            tt = True
            if tf:
                self.HomePage.move(0, 90)
                self.resize(883, 770)
            else:
                self.HomePage.move(0, 60)
                self.resize(883, 745)

    def handleToggleFormat(self):
        global tf

        if tf:
            self.formatbar.hide()
            tf = False
            if tt:
                self.HomePage.move(0, 60)
                self.resize(883, 745)
            else:
                self.HomePage.move(0, 30)
                self.resize(883, 730)
        else:
            self.formatbar.show()
            tf = True
            if tt:
                self.HomePage.move(0, 90)
                self.resize(883, 770)
            else:
                self.HomePage.move(0, 60)
                self.resize(883, 745)

    def handleToggleStatus(self):
        global ts

        if ts:
            self.status.hide()
            ts = False
        else:
            self.status.show()
            ts = True

    # -------- Toolbar slots -----------------------------------

    def New(self):
        self.textEdit.clear()

    def Open(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File')
        try:
            f = open(filename[0], 'r')
            filedata = f.read()
            self.textEdit.setText(filedata)
            f.close()
        except FileNotFoundError:
            self.status.showMessage("No such File has been found.")
        except UnicodeDecodeError:
            QMessageBox.warning(self,"Error","File format not supported")
            self.status.showMessage("File format not supported.")

    def Save(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')
        try:
            f = open(filename[0], 'w')
            filedata = self.textEdit.toPlainText()
            f.write(filedata)
            f.close()
            self.Saved = True
        except FileNotFoundError:
            self.status.showMessage("File Not Saved.")

    def PageView(self):
        preview = QPrintPreviewDialog()
        preview.paintRequested.connect(self.PaintPageView)
        preview.exec_()

    def Print(self):
        dialog = QPrintDialog()
        if dialog.exec_() == QDialog.Accepted:
            self.textEdit.document().print_(dialog.printer())

    def PDF(self):
        printer = QPrinter()
        printer.setOutputFormat(printer.NativeFormat)

        dialog = QPrintDialog(printer)
        dialog.setOption(dialog.PrintToFile)
        if dialog.exec_() == QDialog.Accepted:
            self.textEdit.document().print_(dialog.printer())

    def PaintPageView(self, printer):
        self.textEdit.print_(printer)

    def Find(self):
        global f

        find = Find(self)
        find.show()

        def handleFind():

            f = find.te.toPlainText()
            print(f)

            if cs is True and wwo is False:
                flag = QTextDocument.FindBackward and QTextDocument.FindCaseSensitively

            elif cs is False and wwo is False:
                flag = QTextDocument.FindBackward

            elif cs is False and wwo is True:
                flag = QTextDocument.FindBackward and QTextDocument.FindWholeWords

            elif cs is True and wwo is True:
                flag = QTextDocument.FindBackward and QTextDocument.FindCaseSensitively and QTextDocument.FindWholeWords

            self.textEdit.find(f, flag)

        def handleReplace():
            f = find.te.toPlainText()
            r = find.rp.toPlainText()

            text = self.textEdit.toPlainText()

            newText = text.replace(f, r)

            self.textEdit.clear()
            self.textEdit.append(newText)

        find.src.clicked.connect(handleFind)
        find.rpb.clicked.connect(handleReplace)

    def Undo(self):
        self.textEdit.undo()

    def Redo(self):
        self.textEdit.redo()

    def Cut(self):
        self.textEdit.cut()

    def Copy(self):
        self.textEdit.copy()

    def Paste(self):
        self.textEdit.paste()

    def CursorPosition(self):
        line = self.textEdit.textCursor().blockNumber()
        col = self.textEdit.textCursor().columnNumber()
        linecol = ("Line: " + str(line) + " | " + "Column: " + str(col))
        self.status.showMessage(linecol)

    def FontFamily(self, font):
        font = QFont(self.fontFamily.currentFont())
        self.textEdit.setCurrentFont(font)

    def FontSize(self, fsize):
        size = (int(fsize))
        self.textEdit.setFontPointSize(size)

    def FontColor(self):
        c = QColorDialog.getColor()

        self.textEdit.setTextColor(c)

    def FontBackColor(self):
        c = QColorDialog.getColor()
        self.textEdit.setTextBackgroundColor(c)

    def Bold(self):
        w = self.textEdit.fontWeight()
        if w == 50:
            self.textEdit.setFontWeight(QFont.Bold)
        elif w == 75:
            self.textEdit.setFontWeight(QFont.Normal)

    def Italic(self):
        i = self.textEdit.fontItalic()

        if not i:
            self.textEdit.setFontItalic(True)
        elif i:
            self.textEdit.setFontItalic(False)

    def Underl(self):
        ul = self.textEdit.fontUnderline()

        if not ul:
            self.textEdit.setFontUnderline(True)
        elif ul:
            self.textEdit.setFontUnderline(False)

    def lThrough(self):
        lt = QFont.style()

    def alignLeft(self):
        self.textEdit.setAlignment(Qt.AlignLeft)

    def alignRight(self):
        self.textEdit.setAlignment(Qt.AlignRight)

    def alignCenter(self):
        self.textEdit.setAlignment(Qt.AlignCenter)

    def alignJustify(self):
        self.textEdit.setAlignment(Qt.AlignJustify)

    def Indent(self):
        tab = "\t"
        cursor = self.textEdit.textCursor()

        start = cursor.selectionStart()
        end = cursor.selectionEnd()

        cursor.setPosition(end)
        cursor.movePosition(cursor.EndOfLine)
        end = cursor.position()

        cursor.setPosition(start)
        cursor.movePosition(cursor.StartOfLine)
        start = cursor.position()

        while cursor.position() < end:
            global var

            print(cursor.position(), end)

            cursor.movePosition(cursor.StartOfLine)
            cursor.insertText(tab)
            cursor.movePosition(cursor.Down)
            end += len(tab)

            '''if cursor.position() == end:
                var +=1

            if var == 2:
                break'''
        return

    def Dedent(self):
        tab = "\t"
        cursor = self.textEdit.textCursor()

        start = cursor.selectionStart()
        end = cursor.selectionEnd()

        cursor.setPosition(end)
        cursor.movePosition(cursor.EndOfLine)
        end = cursor.position()

        cursor.setPosition(start)
        cursor.movePosition(cursor.StartOfLine)
        start = cursor.position()

        while cursor.position() < end:
            global var

            cursor.movePosition(cursor.StartOfLine)
            cursor.deleteChar()
            cursor.movePosition(cursor.EndOfLine)
            cursor.movePosition(cursor.Down)
            end -= len(tab)

            '''if cursor.position() == end:
                var +=1

            if var == 2:
                break'''
        return

    def clear(self):
        rows = self.Memory_Widget.rowCount()
        for i in range(rows):
            self.Memory_Widget.setItem(i, 0, QTableWidgetItem(''))
            self.Memory_Widget.setItem(i, 1, QTableWidgetItem(''))
        return

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "8085 Simulator"))
        self.CodeBox.setTitle(_translate("MainWindow", "Code"))
        self.ExecuteButton.setText(_translate("MainWindow", "Execute"))
        self.AssembleButton.setText(_translate("MainWindow", "Assemble"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Editor"))
        self.RunAllBtn.setText(_translate("MainWindow", "Run Whole"))
        self.StepExecBtn.setText(_translate("MainWindow", "Step By Step"))
        item = self.MemHexTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Address"))
        item = self.MemHexTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Label"))
        item = self.MemHexTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mnemonics"))
        item = self.MemHexTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Hex Code"))
        __sortingEnabled = self.MemHexTable.isSortingEnabled()
        self.MemHexTable.setSortingEnabled(False)
        self.MemHexTable.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Assembler"))
        self.OutputBox.setTitle(_translate("MainWindow", "Output"))

        for i in range(8):
            item = self.RegisterContentWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", str(i + 1)))

        item = self.RegisterContentWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Registers"))
        item = self.RegisterContentWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))

        __sortingEnabled = self.RegisterContentWidget.isSortingEnabled()
        self.RegisterContentWidget.setSortingEnabled(False)

        verticalHeaders = ["Accumulator(A)", "Register B", "Register C", "Register D", "Register E", "Register H", "Register L", "Register M"]
        for i, data in enumerate(verticalHeaders):
            item = self.RegisterContentWidget.item(i, 0)
            item.setText(_translate("MainWindow", data))

        self.RegisterContentWidget.setSortingEnabled(__sortingEnabled)
        for i in range(6):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", "New Row"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Register Pairs"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        verticalHeader = ["Program Status Word", "BC", "DE", "HL", "Stack Pointer", "Program Counter(PC)"]
        for i, data in enumerate(verticalHeader):
            item = self.tableWidget.item(i, 0)
            item.setText(_translate("MainWindow", data))

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.FlagContentWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))

        flag = [
            'S', 'Z', '*', 'AC', '*', 'PC', '*', 'CY'
        ]
        for i in range(8):
            item = self.FlagContentWidget.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", flag[i]))

        self.DisplayTab.setTabText(self.DisplayTab.indexOf(self.Registers_tab_2), _translate("MainWindow", "Registers"))

        for i in range(30):
            item = self.Memory_Widget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", str(i + 1)))

        item = self.Memory_Widget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mem. Address"))
        item = self.Memory_Widget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        self.ClrMemory.setText(_translate("MainWindow", "Clear"))
        self.DisplayTab.setTabText(self.DisplayTab.indexOf(self.Memory_tab_2), _translate("MainWindow", "Memory"))
        self.WarningLabel.setText(_translate("MainWindow", "Warning: "))

    def initUI(self):
        self.resize(883, 730)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(883, 0))
        self.setMaximumSize(QtCore.QSize(16777215, 780))
        self.setWindowIcon(QIcon('icons/window_icon.png'))

        # ------- Toolbar --------------------------------------

        # -- Upper Toolbar --

        newAction = QAction(QIcon("icons/new.png"), "New", self)
        newAction.setShortcut("Ctrl+N")
        newAction.setStatusTip("Create a new document from scratch.")
        newAction.triggered.connect(self.New)

        openAction = QAction(QIcon("icons/open.png"), "Open file", self)
        openAction.setStatusTip("Open existing document")
        openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.Open)

        saveAction = QAction(QIcon("icons/save.png"), "Save", self)
        saveAction.setStatusTip("Save document")
        saveAction.setShortcut("Ctrl+S")
        saveAction.triggered.connect(self.Save)

        previewAction = QAction(QIcon("icons/2x/preview.png"), "Page view", self)
        previewAction.setStatusTip("Preview page before printing")
        previewAction.setShortcut("Ctrl+Shift+P")
        previewAction.triggered.connect(self.PageView)

        findAction = QAction(QIcon("icons/find.png"), "Find", self)
        findAction.setStatusTip("Find words in your document")
        findAction.setShortcut("Ctrl+F")
        findAction.triggered.connect(self.Find)

        cutAction = QAction(QIcon("icons/cut.png"), "Cut to clipboard", self)
        cutAction.setStatusTip("Delete and copy text to clipboard")
        cutAction.setShortcut("Ctrl+X")
        cutAction.triggered.connect(self.Cut)

        copyAction = QAction(QIcon("icons/copy.png"), "Copy to clipboard", self)
        copyAction.setStatusTip("Copy text to clipboard")
        copyAction.setShortcut("Ctrl+C")
        copyAction.triggered.connect(self.Copy)

        pasteAction = QAction(QIcon("icons/paste1.png"), "Paste from clipboard", self)
        pasteAction.setStatusTip("Paste text from clipboard")
        pasteAction.setShortcut("Ctrl+V")
        pasteAction.triggered.connect(self.Paste)

        undoAction = QAction(QIcon("icons/undo.png"), "Undo last action", self)
        undoAction.setStatusTip("Undo last action")
        undoAction.setShortcut("Ctrl+Z")
        undoAction.triggered.connect(self.Undo)

        redoAction = QAction(QIcon("icons/redo.png"), "Redo last undone thing", self)
        redoAction.setStatusTip("Redo last undone thing")
        redoAction.setShortcut("Ctrl+Y")
        redoAction.triggered.connect(self.Redo)

        printAction = QAction(QIcon("icons/print.png"), "Print document", self)
        printAction.setStatusTip("Print document")
        printAction.setShortcut("Ctrl+P")
        printAction.triggered.connect(self.Print)

        quitAction = QAction("Close", self)
        quitAction.setShortcut("Alt+F4")
        quitAction.triggered.connect(self.close)

        numberConverterAction = QAction("Number Converter", self)
        numberConverterAction.triggered.connect(self.openNumberConverter)

        self.toolbar = self.addToolBar("Options")
        self.toolbar.addAction(newAction)
        self.toolbar.addAction(openAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(printAction)
        # self.toolbar.addAction(pdfAction)
        self.toolbar.addAction(previewAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(findAction)
        self.toolbar.addAction(cutAction)
        self.toolbar.addAction(copyAction)
        self.toolbar.addAction(pasteAction)
        self.toolbar.addAction(undoAction)
        self.toolbar.addAction(redoAction)
        self.toolbar.addSeparator()
        self.toolbar.addSeparator()
        self.toolbar.hide()

        self.addToolBarBreak()

        # -- Lower Toolbar --

        self.fontFamily = QFontComboBox(self)
        self.fontFamily.currentFontChanged.connect(self.FontFamily)

        fontSize = QComboBox(self)
        fontSize.setEditable(True)
        fontSize.setMinimumContentsLength(3)
        flist = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 22, 24, 26, 28, 32, 36, 40, 44, 48]
        for i in flist:
            fontSize.addItem(str(i))
        fontSize.activated.connect(self.FontSize)

        fontColor = QAction(QIcon("icons/2x/color.png"), "Change font color", self)
        fontColor.triggered.connect(self.FontColor)

        boldAction = QAction(QIcon("icons/bold.png"), "Bold", self)
        boldAction.triggered.connect(self.Bold)

        italicAction = QAction(QIcon("icons/1x/italic.png"), "Italic", self)
        italicAction.triggered.connect(self.Italic)

        underlAction = QAction(QIcon("icons/1x/underline.png"), "Underline", self)
        underlAction.triggered.connect(self.Underl)

        alignLeft = QAction(QIcon("icons/1x/alignLeft.png"), "Align left", self)
        alignLeft.triggered.connect(self.alignLeft)

        alignCenter = QAction(QIcon("icons/1x/alignCenter.png"), "Align center", self)
        alignCenter.triggered.connect(self.alignCenter)

        alignRight = QAction(QIcon("icons/1x/alignRight.png"), "Align right", self)
        alignRight.triggered.connect(self.alignRight)

        alignJustify = QAction(QIcon("icons/1x/alignJustify.png"), "Align justify", self)
        alignJustify.triggered.connect(self.alignJustify)

        indentAction = QAction(QIcon("icons/1x/indent.png"), "Indent Area", self)
        indentAction.setShortcut("Ctrl+Tab")
        indentAction.triggered.connect(self.Indent)

        dedentAction = QAction(QIcon("icons/1x/dedent.png"), "Dedent Area", self)
        dedentAction.setShortcut("Shift+Tab")
        dedentAction.triggered.connect(self.Dedent)

        backColor = QAction(QIcon("icons/1x/backcolor.png"), "Change background color", self)
        backColor.triggered.connect(self.FontBackColor)

        space1 = QLabel("  ", self)
        space2 = QLabel(" ", self)
        space3 = QLabel(" ", self)

        self.formatbar = self.addToolBar("Format")
        self.formatbar.addWidget(self.fontFamily)
        self.formatbar.addWidget(space1)
        self.formatbar.addWidget(fontSize)
        self.formatbar.addWidget(space2)

        self.formatbar.addSeparator()

        self.formatbar.addAction(fontColor)
        self.formatbar.addAction(backColor)

        self.formatbar.addSeparator()

        self.formatbar.addAction(boldAction)
        self.formatbar.addAction(italicAction)
        self.formatbar.addAction(underlAction)

        self.formatbar.addSeparator()

        self.formatbar.addAction(alignLeft)
        self.formatbar.addAction(alignCenter)
        self.formatbar.addAction(alignRight)
        self.formatbar.addAction(alignJustify)

        self.formatbar.addSeparator()

        self.formatbar.addAction(indentAction)
        self.formatbar.addAction(dedentAction)
        self.formatbar.hide()

        # ------- Statusbar ------------------------------------

        self.status = self.statusBar()

        # ------- Menubar --------------------------------------
        self.menubar = self.menuBar()
        file = self.menubar.addMenu("File")
        edit = self.menubar.addMenu("Edit")
        view = self.menubar.addMenu("View")
        self.tools = self.menubar.addMenu("Tools")
        self.settings = self.menubar.addMenu("Settings")

        file.addAction(newAction)
        file.addAction(openAction)
        file.addAction(saveAction)
        file.addAction(printAction)
        file.addAction(previewAction)
        file.addAction(quitAction)

        edit.addAction(undoAction)
        edit.addAction(redoAction)
        edit.addAction(cutAction)
        edit.addAction(copyAction)
        edit.addAction(findAction)

        toggleTool = QAction("Toolbar", self, checkable=True)
        toggleTool.triggered.connect(self.handleToggleTool)

        toggleFormat = QAction("Formatbar", self, checkable=True)
        toggleFormat.triggered.connect(self.handleToggleFormat)

        toggleStatus = QAction("Statusbar", self, checkable=True)
        toggleStatus.triggered.connect(self.handleToggleStatus)

        view.addAction(toggleTool)
        view.addAction(toggleFormat)
        view.addAction(toggleStatus)

        self.tools.addAction(numberConverterAction)

        # ------------- CentralWidget -----------------------------------
        self.centralwidget = QWidget(self)
        # ------------- HomePage Frame -----------------------------------
        self.HomePage = QFrame(self)
        self.HomePage.setGeometry(QtCore.QRect(0, 60, 881, 701))
        self.HomePage.setFrameShape(QFrame.StyledPanel)
        self.HomePage.setFrameShadow(QFrame.Raised)
        self.handleToggleFormat()
        self.handleToggleTool()
        self.handleToggleStatus()
        self.HomePage.move(0, 30)

        # ------------- CodeBox -----------------------------------
        self.CodeBox = QGroupBox(self.HomePage)
        self.CodeBox.setGeometry(QtCore.QRect(7, 5, 511, 627))
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.CodeBox.setFont(font)

        # ------------- TabWidget -----------------------------------
        self.tabWidget = QTabWidget(self.CodeBox)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 494, 597))
        self.tabWidget.setUsesScrollButtons(False)

        # ------------- Tab -----------------------------------
        self.tab = QWidget()

        self.gridLayout = QGridLayout(self.tab)

        self.ExecuteButton = QPushButton(self.tab)
        self.ExecuteButton.setMinimumSize(QtCore.QSize(0, 48))
        self.gridLayout.addWidget(self.ExecuteButton, 1, 0, 1, 1)

        self.AssembleButton = QPushButton(self.tab)
        self.AssembleButton.setMinimumSize(QtCore.QSize(0, 48))
        self.gridLayout.addWidget(self.AssembleButton, 1, 1, 1, 1)

        self.textEdit = MyTextEdit(self.tab)
        font = QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.textEdit.cursorPositionChanged.connect(self.CursorPosition)

        # ------------- tab_2 -----------------------------------
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.RunAllBtn = QPushButton(self.tab_2)
        self.RunAllBtn.setMinimumSize(QtCore.QSize(0, 48))
        self.gridLayout_2.addWidget(self.RunAllBtn, 1, 0, 1, 1)
        self.StepExecBtn = QPushButton(self.tab_2)
        self.StepExecBtn.setMinimumSize(QtCore.QSize(0, 48))
        self.gridLayout_2.addWidget(self.StepExecBtn, 1, 1, 1, 1)

        # ------------- MemHexTable -----------------------------------
        self.MemHexTable = QTableWidget(self.tab_2)
        self.MemHexTable.setFrameShape(QFrame.Box)
        self.MemHexTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MemHexTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.MemHexTable.setAutoScrollMargin(16)
        self.MemHexTable.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.MemHexTable.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.MemHexTable.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.MemHexTable.setIconSize(QtCore.QSize(0, 0))
        self.MemHexTable.setRowCount(30)
        self.MemHexTable.setColumnCount(4)
        self.MemHexTable.setObjectName("MemHexTable")
        for i in range(4):
            item = QTableWidgetItem()
            self.MemHexTable.setHorizontalHeaderItem(i, item)

        for i in range(30):
            item = QTableWidgetItem()
            self.MemHexTable.setItem(0, i, item)

        self.MemHexTable.horizontalHeader().setCascadingSectionResizes(True)
        self.MemHexTable.horizontalHeader().setDefaultSectionSize(112)
        self.MemHexTable.horizontalHeader().setHighlightSections(True)
        self.MemHexTable.horizontalHeader().setSortIndicatorShown(False)
        self.MemHexTable.horizontalHeader().setStretchLastSection(True)
        self.MemHexTable.verticalHeader().setVisible(False)
        self.MemHexTable.verticalHeader().setCascadingSectionResizes(False)
        self.MemHexTable.verticalHeader().setDefaultSectionSize(30)
        self.MemHexTable.verticalHeader().setMinimumSectionSize(21)
        self.gridLayout_2.addWidget(self.MemHexTable, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")

        # ------------- OutputBox -----------------------------------
        self.OutputBox = QGroupBox(self.HomePage)
        self.OutputBox.setGeometry(QtCore.QRect(526, 5, 337, 627))
        self.OutputBox.setMaximumSize(QtCore.QSize(16777215, 627))
        font = QFont()
        font.setPointSize(9)
        self.OutputBox.setFont(font)
        self.OutputBox.setLayoutDirection(QtCore.Qt.LeftToRight)

        # ------------- DisplayTab -----------------------------------
        self.DisplayTab = QTabWidget(self.OutputBox)
        self.DisplayTab.setGeometry(QtCore.QRect(7, 23, 325, 595))
        self.DisplayTab.setMinimumSize(QtCore.QSize(323, 590))
        self.DisplayTab.setMaximumSize(QtCore.QSize(325, 595))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.DisplayTab.setFont(font)
        self.DisplayTab.setCursor(QCursor(QtCore.Qt.ArrowCursor))
        self.DisplayTab.setAutoFillBackground(False)
        self.DisplayTab.setTabShape(QTabWidget.Triangular)

        # ------------- RegisterContentWidget -----------------------------------
        self.Registers_tab_2 = QWidget()
        self.verticalLayout_2 = QVBoxLayout(self.Registers_tab_2)
        self.RegisterContentWidget = QTableWidget(self.Registers_tab_2)
        self.RegisterContentWidget.setMinimumSize(QtCore.QSize(275, 230))
        self.RegisterContentWidget.setMaximumSize(QtCore.QSize(300, 230))
        self.RegisterContentWidget.setStyleSheet("QTableView::item\n"
                                                 "{\n"
                                                 "text-align : right;\n"
                                                 "}")
        self.RegisterContentWidget.setFrameShape(QFrame.StyledPanel)
        self.RegisterContentWidget.setFrameShadow(QFrame.Plain)
        self.RegisterContentWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RegisterContentWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RegisterContentWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.RegisterContentWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.RegisterContentWidget.setObjectName("RegisterContentWidget")
        self.RegisterContentWidget.setColumnCount(2)
        self.RegisterContentWidget.setRowCount(8)
        for i in range(8):
            item = QTableWidgetItem()
            self.RegisterContentWidget.setVerticalHeaderItem(i, item)

        item = QTableWidgetItem()
        self.RegisterContentWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.RegisterContentWidget.setHorizontalHeaderItem(1, item)

        for i in range(8):
            item = QTableWidgetItem()
            self.RegisterContentWidget.setItem(i, 0, item)

        self.RegisterContentWidget.horizontalHeader().setDefaultSectionSize(132)
        self.RegisterContentWidget.horizontalHeader().setStretchLastSection(True)
        self.RegisterContentWidget.verticalHeader().setVisible(False)
        self.RegisterContentWidget.verticalHeader().setDefaultSectionSize(25)
        self.RegisterContentWidget.verticalHeader().setHighlightSections(False)
        self.RegisterContentWidget.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.RegisterContentWidget)

        # ------------- tableWidget -----------------------------------
        self.tableWidget = QTableWidget(self.Registers_tab_2)
        self.tableWidget.setMinimumSize(QtCore.QSize(245, 200))
        self.tableWidget.setMaximumSize(QtCore.QSize(300, 210))
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(6)
        for i in range(6):
            item = QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        for i in range(6):
            item = QTableWidgetItem()
            self.tableWidget.setItem(i, 0, item)

        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(132)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableWidget)

        # ------------- FlagContentWidget -----------------------------------
        self.FlagContentWidget = QTableWidget(self.Registers_tab_2)
        self.FlagContentWidget.setMinimumSize(QtCore.QSize(303, 78))
        self.FlagContentWidget.setMaximumSize(QtCore.QSize(310, 80))
        self.FlagContentWidget.setFrameShape(QFrame.StyledPanel)
        self.FlagContentWidget.setFrameShadow(QFrame.Plain)
        self.FlagContentWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.FlagContentWidget.setColumnCount(8)
        self.FlagContentWidget.setRowCount(1)
        for i in range(8):
            item = QTableWidgetItem()
            self.FlagContentWidget.setHorizontalHeaderItem(i, item)
        item = QTableWidgetItem()
        self.FlagContentWidget.setVerticalHeaderItem(0, item)

        self.FlagContentWidget.horizontalHeader().setVisible(True)
        self.FlagContentWidget.horizontalHeader().setDefaultSectionSize(35)
        self.FlagContentWidget.horizontalHeader().setMinimumSectionSize(39)
        self.FlagContentWidget.verticalHeader().setVisible(False)
        self.FlagContentWidget.verticalHeader().setDefaultSectionSize(33)
        self.FlagContentWidget.verticalHeader().setHighlightSections(True)
        self.FlagContentWidget.verticalHeader().setMinimumSectionSize(23)
        self.verticalLayout_2.addWidget(self.FlagContentWidget)
        self.DisplayTab.addTab(self.Registers_tab_2, "")

        # ------------- Memory_tab_2 -----------------------------------
        self.Memory_tab_2 = QWidget()
        self.verticalLayout = QVBoxLayout(self.Memory_tab_2)

        # ------------- Memory_Widget -----------------------------------
        self.Memory_Widget = QTableWidget(self.Memory_tab_2)
        self.Memory_Widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Memory_Widget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.Memory_Widget.setColumnCount(2)
        self.Memory_Widget.setRowCount(30)
        for i in range(30):
            item = QTableWidgetItem()
            self.Memory_Widget.setVerticalHeaderItem(i, item)

        item = QTableWidgetItem()
        self.Memory_Widget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.Memory_Widget.setHorizontalHeaderItem(1, item)

        self.Memory_Widget.horizontalHeader().setCascadingSectionResizes(True)
        self.Memory_Widget.horizontalHeader().setDefaultSectionSize(130)
        self.Memory_Widget.horizontalHeader().setStretchLastSection(True)
        self.Memory_Widget.verticalHeader().setVisible(False)
        self.Memory_Widget.verticalHeader().setHighlightSections(True)
        self.verticalLayout.addWidget(self.Memory_Widget)

        # ------------- ClrMemory -----------------------------------
        self.ClrMemory = QPushButton(self.Memory_tab_2)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.ClrMemory.setFont(font)
        self.ClrMemory.setAutoDefault(False)
        self.ClrMemory.setObjectName("ClrMemory")
        self.ClrMemory.clicked.connect(self.clear)
        self.verticalLayout.addWidget(self.ClrMemory)
        self.DisplayTab.addTab(self.Memory_tab_2, "")

        # ------------- WarningLabel -----------------------------------
        self.WarningLabel = QLabel(self.HomePage)
        self.WarningLabel.setGeometry(QtCore.QRect(20, 640, 851, 25))
        font = QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.WarningLabel.setFont(font)

        self.setCentralWidget(self.centralwidget)

        # ------------- others -----------------------------------
        self.retranslateUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.DisplayTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        # self.setStyleSheet(
        #     """
        #     QMainWindow{
        #     background-color: black
        #     }
        #     QLabel{
        #     color: white
        #     }
        #     QGroupBox{
        #     color:black;
        #     background-color: white
        #     }
        #     QTabWidget{
        #     }
        #     QMenuBar{
        #
        #     }
        #     """
        # )


def main():
    app = QApplication(sys.argv)
    main = Ui_MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()