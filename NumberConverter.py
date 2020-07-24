from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialogButtonBox


class MyLineEdit(QtWidgets.QLineEdit):
    editingFinished = QtCore.pyqtSignal()
    receivedFocus = QtCore.pyqtSignal()

    def __init__(self, parent):
        super(MyLineEdit, self).__init__(parent)
        self._changed = False
        self.textChanged.connect(self._handle_text_changed)

    def focusInEvent(self, QFocusEvent):
        super(MyLineEdit, self).focusInEvent(QFocusEvent)
        self.receivedFocus.emit()

    def focusOutEvent(self, QFocusEvent):
        if self._changed:
            self.editingFinished.emit()
        super(MyLineEdit, self).focusOutEvent(QFocusEvent)

    def _handle_text_changed(self):
        self._changed = True

class Ui_NumberConverter(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, None)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.setObjectName("self")
        self.setWindowModality(QtCore.Qt.NonModal)
        self.resize(558, 163)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.Warninglabel = QtWidgets.QLabel(self)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setTitle("")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.NumberConverterLayout = QtWidgets.QVBoxLayout()
        self.NumberConverterLayout.setContentsMargins(5, 15, 5, 15)
        self.NumberConverterLayout.setObjectName("NumberConverterLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.HexadecimalLayout = QtWidgets.QVBoxLayout()
        self.HexadecimalLayout.setContentsMargins(10, 0, 10, 5)
        self.HexadecimalLayout.setObjectName("HexadecimalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.HexadecimalLayout.addWidget(self.label)
        self.Hexadecimal = MyLineEdit(self.groupBox)
        self.HexadecimalLayout.addWidget(self.Hexadecimal)
        self.horizontalLayout.addLayout(self.HexadecimalLayout)
        self.DecimalLayout = QtWidgets.QVBoxLayout()
        self.DecimalLayout.setContentsMargins(10, 0, 10, 5)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.DecimalLayout.addWidget(self.label_2)
        self.Decimal = MyLineEdit(self.groupBox)
        self.DecimalLayout.addWidget(self.Decimal)
        self.horizontalLayout.addLayout(self.DecimalLayout)
        self.BinaryLayout = QtWidgets.QVBoxLayout()
        self.BinaryLayout.setContentsMargins(10, 0, 10, 5)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.BinaryLayout.addWidget(self.label_3)
        self.Binary = MyLineEdit(self.groupBox)
        self.BinaryLayout.addWidget(self.Binary)
        self.horizontalLayout.addLayout(self.BinaryLayout)
        self.NumberConverterLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.NumberConverterLayout.addWidget(self.buttonBox)
        self.gridLayout_2.addLayout(self.NumberConverterLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.Warninglabel, 1, 0, 1, 1)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.convert)
        self.buttonBox.rejected.connect(self.close)
        self.buttonBox.button(QDialogButtonBox.Reset).clicked.connect(self.reset)

        self.Hexadecimal.editingFinished.connect(self.convert)
        self.Binary.editingFinished.connect(self.convert)
        self.Decimal.editingFinished.connect(self.convert)

        self.retranslateUi(self)
        self.setWindowIcon(QIcon("icons/editor.png"))
        QtCore.QMetaObject.connectSlotsByName(self)

    def convert(self):
        hexadecimal = self.Hexadecimal.text()
        decimal = self.Decimal.text()
        binary = self.Binary.text()
        sender = self.sender()

        try:
            if sender == self.Hexadecimal:
                if hexadecimal != '':
                    num = int(hexadecimal, 16)
                    self.Decimal.setText(str(num))
                    self.Binary.setText(bin(num)[2:])
                    return
            if sender == self.Decimal:
                if decimal != '':
                    num = int(decimal)
                    self.Hexadecimal.setText(hex(num)[2:])
                    self.Binary.setText(bin(num)[2:])
                    return
            if sender == self.Binary:
                if binary != '':
                    num = int(binary, 2)
                    self.Decimal.setText(str(num))
                    self.Hexadecimal.setText(hex(num)[2:])
                    return
        except ValueError as e:
            self.Warninglabel.setText(str(e))

    def reset(self):
        self.Hexadecimal.setText('')
        self.Decimal.setText('')
        self.Binary.setText('')
        self.Warninglabel.setText('')

    def retranslateUi(self, NumberConverter):
        _translate = QtCore.QCoreApplication.translate
        NumberConverter.setWindowTitle(_translate("NumberConverter", "Number Converter Tool"))
        self.label.setText(_translate("NumberConverter", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Hexadecimal</span></p></body></html>"))
        self.label_2.setText(_translate("NumberConverter", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Decimal</span></p></body></html>"))
        self.label_3.setText(_translate("NumberConverter", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Binary</span></p></body></html>"))
        self.buttonBox.button(QDialogButtonBox.Reset).setText("Clear")
        self.buttonBox.button(QDialogButtonBox.Ok).setText("Convert")
        self.Warninglabel.setText(_translate("NumberConverter",
                                      "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\"></span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_NumberConverter()
    ui.show()
    ui.exec_()
    sys.exit(app.exec_())
