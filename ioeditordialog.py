import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QApplication, QGridLayout, \
    QLineEdit, QDialogButtonBox, QAbstractItemView


class Ui_IOEditor(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, None)
        self.parent = parent
        self.IOMapper = {}
        self.initUI()

    def initUI(self):
        self.resize(696, 671)
        self.setMinimumSize(QtCore.QSize(691, 0))
        self.setMaximumSize(QtCore.QSize(16777215, 674))
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.PortAddressLabel = QLabel(self)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.PortAddressLabel.setFont(font)
        self.PortAddressLabel.setObjectName("PortAddressLabel")
        self.gridLayout.addWidget(self.PortAddressLabel, 1, 0, 1, 1)
        self.PortAddress = QLineEdit(self)
        self.PortAddress.setObjectName("PortAddress")
        self.gridLayout.addWidget(self.PortAddress, 1, 1, 1, 3)
        self.label = QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.PortValue = QLineEdit(self)
        self.PortValue.setObjectName("PortValue")
        self.gridLayout.addWidget(self.PortValue, 3, 1, 1, 3)
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 2, 1, 1)
        self.enterButton = QPushButton(self)
        self.enterButton.setObjectName("enterButton")
        self.enterButton.clicked.connect(self.input)
        self.gridLayout.addWidget(self.enterButton, 4, 0, 1, 1)

        self.resetButton = QPushButton(self)
        self.resetButton.clicked.connect(self.reset)
        self.gridLayout.addWidget(self.resetButton, 4, 1, 1, 1)

        self.IOBox = QTableWidget(self)
        self.IOBox.setMinimumSize(QtCore.QSize(561, 0))
        self.IOBox.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        self.IOBox.setObjectName("IOBox")
        self.IOBox.setColumnCount(16)
        self.IOBox.setRowCount(16)
        self.IOBox.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setWindowIcon(QIcon("icons/editor.png"))

        for i in range(16):
            item = QTableWidgetItem()
            self.IOBox.setVerticalHeaderItem(i, item)

        for i in range(16):
            item = QTableWidgetItem()
            self.IOBox.setHorizontalHeaderItem(i, item)

        self.IOBox.horizontalHeader().setCascadingSectionResizes(True)
        self.IOBox.horizontalHeader().setDefaultSectionSize(36)
        self.IOBox.horizontalHeader().setSortIndicatorShown(False)
        self.IOBox.horizontalHeader().setStretchLastSection(True)
        self.IOBox.verticalHeader().setCascadingSectionResizes(True)
        self.IOBox.verticalHeader().setDefaultSectionSize(34)
        self.gridLayout.addWidget(self.IOBox, 0, 0, 1, 3)

        # self.setStyleSheet("""
        #     QDialog{
        #     background-color:black
        #     }
        #     QLabel{
        #     color: white
        #     }
        #     QLineEdit{
        #     background-color: white
        #     }
        #
        # """
        # )

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "I/O Port Editor"))
        self.PortAddressLabel.setText(_translate("self", "Enter I/O Port Address: "))
        self.label.setText(_translate("self", "Enter Input Value"))
        self.enterButton.setText(_translate("self", "Enter"))
        self.resetButton.setText(_translate("self", "Reset"))

        verticalHeaders = ["00", "10", "20", "30", "40", "50", "60", "70", "80", "90",
                           "A0", "B0", "C0", "D0", "E0", "F0"]
        for i in range(16):
            item = self.IOBox.verticalHeaderItem(i)
            item.setText(_translate("Dialog", verticalHeaders[i]))

        horizontalHeaders = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        for i in range(16):
            item = self.IOBox.horizontalHeaderItem(i)
            item.setText(_translate("Dialog", horizontalHeaders[i]))

        for row in range(16):
            for col in range(16):
                self.IOBox.setItem(row, col, QTableWidgetItem("-"))

        # self.fillItems()
        return

    def input(self):
        address = self.PortAddress.text().upper()
        value = self.PortValue.text().upper()
        if len(address) != 2 or len(value) != 2:
            return
        try:
            num = int(address, 16)
            num2 = int(value, 16)
            row = num // 16
            col = num % 16
            self.IOBox.setItem(row, col, QTableWidgetItem(value))
            self.IOMapper[address] = value
        except ValueError:
            return

    def reset(self):
        for row in range(16):
            for col in range(16):
                self.IOBox.setItem(row, col, QTableWidgetItem("-"))

    def fillItems(self):
        for index, key in enumerate(self.parent.IOMapper):
            address = int(key, 16)
            value = self.parent.IOMapper[key]
            row = address // 16
            col = address % 16
            self.IOBox.setItem(row, col, QTableWidgetItem(value))

    def exec_(self):
        self.parent.IOMapper = self.IOMapper
        super(Ui_IOEditor, self).exec_()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_IOEditor()
    ui.show()
    sys.exit(app.exec_())
