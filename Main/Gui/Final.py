# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final(temp1).ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self,MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.Editor_tab = QtWidgets.QWidget()
        self.AssembleBtn = QtWidgets.QPushButton(self.Editor_tab)
        self.CorrectBtn = QtWidgets.QPushButton(self.Editor_tab)
        self.textEdit = QtWidgets.QTextEdit(self.Editor_tab)
        self.Assembler_tab = QtWidgets.QWidget()
        self.groupBox_3 = QtWidgets.QGroupBox(self.Assembler_tab)
        self.RunAllBtn = QtWidgets.QPushButton(self.Assembler_tab)
        self.pushButton_2 = QtWidgets.QPushButton(self.Assembler_tab)
        self.MemHexTable = QtWidgets.QTableWidget(self.Assembler_tab)

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.DisplayTab = QtWidgets.QTabWidget(self.groupBox_2)
        self.Registers_tab = QtWidgets.QWidget()
        self.Register_Contents = QtWidgets.QGroupBox(self.Registers_tab)
        self.RegisterContentWidget = QtWidgets.QTableWidget(self.Register_Contents)
        self.groupBox_4 = QtWidgets.QGroupBox(self.Register_Contents)
        self.FlagContentWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.Memory_tab = QtWidgets.QWidget()
        self.Memory_Widget = QtWidgets.QTableWidget(self.Memory_tab)
        self.menubar = QtWidgets.QMenuBar(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 678)
##        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
##        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(4, 10, 501, 591))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
##        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 481, 551))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
##        self.Editor_tab = QtWidgets.QWidget()
        self.Editor_tab.setObjectName("Editor_tab")
##        self.AssembleBtn = QtWidgets.QPushButton(self.Editor_tab)
        self.AssembleBtn.setGeometry(QtCore.QRect(273, 450, 170, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.AssembleBtn.setFont(font)
        self.AssembleBtn.setStyleSheet("")
        self.AssembleBtn.setObjectName("AssembleBtn")
##        self.CorrectBtn = QtWidgets.QPushButton(self.Editor_tab)
        self.CorrectBtn.setGeometry(QtCore.QRect(20, 450, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        
        self.CorrectBtn.setFont(font)
        self.CorrectBtn.setAutoFillBackground(False)
        self.CorrectBtn.setStyleSheet("padding:10px 30px 10px 30px")
        self.CorrectBtn.setAutoDefault(True)
        self.CorrectBtn.setDefault(False)
        self.CorrectBtn.setFlat(False)
        self.CorrectBtn.setObjectName("CorrectBtn")
        
        
##        self.textEdit = QtWidgets.QTextEdit(self.Editor_tab)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 472, 421))
        self.textEdit.setStyleSheet("border: 1px black;")
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.Editor_tab, "")
        
##        self.Assembler_tab = QtWidgets.QWidget()
        self.Assembler_tab.setObjectName("Assembler_tab")
        self.tabWidget.addTab(self.Assembler_tab, "")
        
##        self.pushButton = QtWidgets.QPushButton(self.Assembler_tab)
        self.RunAllBtn.setGeometry(QtCore.QRect(30, 460, 185, 51))
        
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        
        self.RunAllBtn.setFont(font)
        self.RunAllBtn.setObjectName("RunAllBtn")
        
##        self.pushButton_2 = QtWidgets.QPushButton(self.Assembler_tab)
        self.pushButton_2.setGeometry(QtCore.QRect(273, 460, 172, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        
##        self.MemHexTable = QtWidgets.QTableWidget(self.Assembler_tab)
        self.MemHexTable.setGeometry(QtCore.QRect(0, 0, 471, 421))
        self.MemHexTable.setFrameShape(QtWidgets.QFrame.Box)
        self.MemHexTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.MemHexTable.setAutoScrollMargin(16)
        self.MemHexTable.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.MemHexTable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.MemHexTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.MemHexTable.setIconSize(QtCore.QSize(0, 0))
        #self.MemHexTable.setRowCount(15)
        self.MemHexTable.setColumnCount(7)
        self.MemHexTable.setObjectName("MemHexTable")

        item = QtWidgets.QTableWidgetItem()
        self.MemHexTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.MemHexTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.MemHexTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.MemHexTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.MemHexTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.MemHexTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.MemHexTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.MemHexTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.MemHexTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.MemHexTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.MemHexTable.setItem(1, 2, item)
        
        self.MemHexTable.horizontalHeader().setCascadingSectionResizes(False)
        self.MemHexTable.horizontalHeader().setDefaultSectionSize(65)
        self.MemHexTable.horizontalHeader().setHighlightSections(True)
        self.MemHexTable.horizontalHeader().setSortIndicatorShown(False)
        self.MemHexTable.horizontalHeader().setStretchLastSection(False)
        self.MemHexTable.verticalHeader().setVisible(False)
        self.MemHexTable.verticalHeader().setCascadingSectionResizes(False)
        self.MemHexTable.verticalHeader().setDefaultSectionSize(30)
        self.MemHexTable.verticalHeader().setMinimumSectionSize(21)

##        self.groupBox_3 = QtWidgets.QGroupBox(self.Assembler_tab)
        self.groupBox_3.setGeometry(QtCore.QRect(8, 430, 460, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        

##        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 10, 331, 591))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")

##        self.DisplayTab = QtWidgets.QTabWidget(self.groupBox_2)
        self.DisplayTab.setGeometry(QtCore.QRect(12, 30, 311, 461))

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.DisplayTab.setFont(font)
        self.DisplayTab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.DisplayTab.setAutoFillBackground(False)
        self.DisplayTab.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.DisplayTab.setObjectName("DisplayTab")

##        self.Registers_tab = QtWidgets.QWidget()
        self.Registers_tab.setObjectName("Registers_tab")

##        self.Register_Contents = QtWidgets.QGroupBox(self.Registers_tab)
        self.Register_Contents.setGeometry(QtCore.QRect(5, 10, 291, 391))
        self.Register_Contents.setObjectName("Register_Contents")

##        self.RegisterContentWidget = QtWidgets.QTableWidget(self.Register_Contents)
        self.RegisterContentWidget.setGeometry(QtCore.QRect(4, 30, 281, 221))
        self.RegisterContentWidget.setMaximumSize(QtCore.QSize(281, 16777215))
        self.RegisterContentWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RegisterContentWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RegisterContentWidget.setObjectName("RegisterContentWidget")
        self.RegisterContentWidget.setColumnCount(2)
        self.RegisterContentWidget.setRowCount(8)
        self.RegisterContentWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RegisterContentWidget.setItem(7, 0, item)
        self.RegisterContentWidget.horizontalHeader().setDefaultSectionSize(139)
        self.RegisterContentWidget.verticalHeader().setVisible(False)
        self.RegisterContentWidget.verticalHeader().setDefaultSectionSize(25)

##        self.groupBox_4 = QtWidgets.QGroupBox(self.Register_Contents)
        self.groupBox_4.setGeometry(QtCore.QRect(7, 270, 278, 80))
        self.groupBox_4.setObjectName("groupBox_4")

##        self.FlagContentWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.FlagContentWidget.setGeometry(QtCore.QRect(6, 20, 267, 71))
        self.FlagContentWidget.setObjectName("FlagContentWidget")
        self.FlagContentWidget.setColumnCount(8)
        self.FlagContentWidget.setRowCount(1)
        self.FlagContentWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.FlagContentWidget.setStyleSheet("background-color:#f4f4f4")

        item = QtWidgets.QTableWidgetItem()
        self.FlagContentWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.FlagContentWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.FlagContentWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.FlagContentWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.FlagContentWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.FlagContentWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.FlagContentWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.FlagContentWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()

        self.FlagContentWidget.setHorizontalHeaderItem(7, item)
        self.FlagContentWidget.horizontalHeader().setDefaultSectionSize(33)
        self.FlagContentWidget.verticalHeader().setVisible(False)
        self.FlagContentWidget.verticalHeader().setHighlightSections(True)

        self.DisplayTab.addTab(self.Registers_tab, "")

##        self.Memory_tab = QtWidgets.QWidget()
        self.Memory_tab.setObjectName("Memory_tab")

##        self.Memory_Widget = QtWidgets.QTableWidget(self.Memory_tab)
        self.Memory_Widget.setGeometry(QtCore.QRect(-1, -1, 311, 441))
        self.Memory_Widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Memory_Widget.setObjectName("Memory_Widget")
        self.Memory_Widget.setColumnCount(2)
        self.Memory_Widget.setRowCount(34)

        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(30, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(31, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(32, item)
        item = QtWidgets.QTableWidgetItem()
        self.Memory_Widget.setVerticalHeaderItem(33, item)
        item = QtWidgets.QTableWidgetItem()

        self.Memory_Widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()

        self.Memory_Widget.setHorizontalHeaderItem(1, item)
        self.Memory_Widget.horizontalHeader().setDefaultSectionSize(147)
        self.Memory_Widget.verticalHeader().setVisible(False)
        self.Memory_Widget.verticalHeader().setHighlightSections(True)
        self.DisplayTab.addTab(self.Memory_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)

##        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 870, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_2)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.DisplayTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AssembleBtn.setText(_translate("MainWindow", "Assemble"))
        self.CorrectBtn.setText(_translate("MainWindow", "Correct"))
        self.CorrectBtn.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Editor_tab), _translate("MainWindow", "Editor"))
        self.RunAllBtn.setText(_translate("MainWindow", "Run All at Once"))
        self.pushButton_2.setText(_translate("MainWindow", "One At a Time"))
        item = self.MemHexTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Address"))
        item = self.MemHexTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Label"))
        item = self.MemHexTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mnemonics"))
        item = self.MemHexTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Hex Code"))
        item = self.MemHexTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Bytes"))
        item = self.MemHexTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "M-cycles"))
        item = self.MemHexTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "T-States"))
        __sortingEnabled = self.MemHexTable.isSortingEnabled()
        self.MemHexTable.setSortingEnabled(False)
        self.MemHexTable.setSortingEnabled(__sortingEnabled)
        self.groupBox_3.setTitle(_translate("MainWindow", "Simulate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Assembler_tab), _translate("MainWindow", "Assembler"))
        self.Register_Contents.setTitle(_translate("MainWindow", "Register Contents"))
        item = self.RegisterContentWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.RegisterContentWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.RegisterContentWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.RegisterContentWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.RegisterContentWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.RegisterContentWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.RegisterContentWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.RegisterContentWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.RegisterContentWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Registers"))
        item = self.RegisterContentWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        __sortingEnabled = self.RegisterContentWidget.isSortingEnabled()
        self.RegisterContentWidget.setSortingEnabled(False)
        item = self.RegisterContentWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Accumulator(A)"))
        item = self.RegisterContentWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Register B"))
        item = self.RegisterContentWidget.item(2, 0)
        item.setText(_translate("MainWindow", "Register C"))
        item = self.RegisterContentWidget.item(3, 0)
        item.setText(_translate("MainWindow", "Register D"))
        item = self.RegisterContentWidget.item(4, 0)
        item.setText(_translate("MainWindow", "Register E"))
        item = self.RegisterContentWidget.item(5, 0)
        item.setText(_translate("MainWindow", "Register H"))
        item = self.RegisterContentWidget.item(6, 0)
        item.setText(_translate("MainWindow", "Register L"))
        item = self.RegisterContentWidget.item(7, 0)
        item.setText(_translate("MainWindow", "Register M"))
        self.RegisterContentWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_4.setTitle(_translate("MainWindow", "Flags"))
        item = self.FlagContentWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.FlagContentWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "S"))
        item = self.FlagContentWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Z"))
        item = self.FlagContentWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "*"))
        item = self.FlagContentWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "AC"))
        item = self.FlagContentWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "*"))
        item = self.FlagContentWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "PC"))
        item = self.FlagContentWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "*"))
        item = self.FlagContentWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "CY"))
        self.DisplayTab.setTabText(self.DisplayTab.indexOf(self.Registers_tab), _translate("MainWindow", "Registers"))
        item = self.Memory_Widget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(21)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(22)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(23)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(24)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(25)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(26)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(27)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(28)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(29)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(30)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(31)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(32)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Memory_Widget.verticalHeaderItem(33)
        item = self.Memory_Widget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mem. Address"))
        item = self.Memory_Widget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        self.DisplayTab.setTabText(self.DisplayTab.indexOf(self.Memory_tab), _translate("MainWindow", "Memory"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSave.setText(_translate("MainWindow", "New"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_2.setText(_translate("MainWindow", "Save"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


