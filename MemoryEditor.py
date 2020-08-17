from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

class Ui_AddressEditor(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, None)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.setObjectName("self")
        self.resize(329, 229)
        self.setMinimumSize(QtCore.QSize(329, 229))
        self.MemoryLabel = QtWidgets.QLabel(self)
        self.MemoryLabel.setGeometry(QtCore.QRect(20, 40, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.MemoryLabel.setFont(font)
        self.MemoryLabel.setObjectName("MemoryLabel")
        self.StackLabel = QtWidgets.QLabel(self)
        self.StackLabel.setGeometry(QtCore.QRect(20, 110, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.StackLabel.setFont(font)
        self.StackLabel.setObjectName("StackLabel")
        self.MemoryStart = QtWidgets.QLineEdit(self)
        self.MemoryStart.setGeometry(QtCore.QRect(223, 38, 70, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.MemoryStart.setFont(font)
        self.MemoryStart.setObjectName("MemoryStart")
        self.SpLocation = QtWidgets.QLineEdit(self)
        self.SpLocation.setGeometry(QtCore.QRect(223, 108, 70, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.SpLocation.setFont(font)
        self.SpLocation.setObjectName("SpLocation")
        self.ErrorLabel = QtWidgets.QLabel(self)
        self.ErrorLabel.setGeometry(QtCore.QRect(20, 160, 292, 16))
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(300, 40, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(300, 110, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.OkButton = QtWidgets.QPushButton(self)
        self.OkButton.setGeometry(QtCore.QRect(120, 190, 75, 23))
        self.OkButton.setObjectName("OkButton")
        self.OkButton.clicked.connect(self.input)

        self.CancelButton = QtWidgets.QPushButton(self)
        self.CancelButton.setGeometry(QtCore.QRect(220, 190, 75, 23))
        self.CancelButton.setObjectName("CancelButton")
        self.CancelButton.clicked.connect(self.reject)

        self.retranslateUi()
        self.setWindowIcon(QIcon("icons/editor.png"))
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Memory Editor"))
        self.MemoryLabel.setText(_translate("self", "Enter Memory Start Address:"))
        self.StackLabel.setText(_translate("self", "Enter Stack Pointer Location:"))
        self.MemoryStart.setText(_translate("self", "0000"))
        self.SpLocation.setText(_translate("self", "FFFF"))
        self.ErrorLabel.setText(_translate("self", "*"))
        self.label_2.setText(_translate("self", "H"))
        self.label_3.setText(_translate("self", "H"))
        self.OkButton.setText(_translate("self", "OK"))
        self.CancelButton.setText(_translate("self", "Cancel"))

    def input(self):
        memoryaddress = self.MemoryStart.text().upper()
        pointerlocation = self.SpLocation.text().upper()
        try:
            if len(memoryaddress) != 4 or len(pointerlocation) != 4:
                raise Exception("Address Not Valid. ")
            num = int(memoryaddress, 16)
            num = int(pointerlocation, 16)

        except ValueError:
            self.ErrorLabel.setText("Invalid Literal for 16-bit hexadecimal address.")
            return
        except Exception as e:
            self.ErrorLabel.setText(str(e))
            return
        self.close()

    def closeEvent(self, event):
        self.parent.MemoryStartAddress = self.MemoryStart.text().upper()
        self.parent.StackPointerAddress = self.SpLocation.text().upper()
        self.parent.updateAddresses()
