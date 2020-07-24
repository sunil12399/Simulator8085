# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saveonexit.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# Sunil's exit
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialogButtonBox


# class Ui_ExitDialog(QtWidgets.QDialog):
#     def __init__(self, parent=None):
#         QtWidgets.QDialog.__init__(self, None)
#         self.parent = parent
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowModality(QtCore.Qt.ApplicationModal)
#         self.resize(587, 142)
#         self.setMinimumSize(QtCore.QSize(587, 0))
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap("Main/Gui/icons/find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.setWindowIcon(icon)
#
#         self.label = QtWidgets.QLabel(self)
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.label.setFont(font)
#
#         Qbtn = QDialogButtonBox.Ok | QDialogButtonBox.No | QDialogButtonBox.Cancel
#         self.buttonBox = QDialogButtonBox(Qbtn)
#         self.buttonBox.accepted.connect(self.accept)
#         self.buttonBox.rejected.connect(self.reject)
#
#         self.verticalLayout = QtWidgets.QVBoxLayout()
#         self.verticalLayout.addWidget(self.label)
#         self.verticalLayout.addWidget(self.buttonBox)
#         self.setLayout(self.verticalLayout)
#
#         self.retranslateUi(self)
#         QtCore.QMetaObject.connectSlotsByName(self)
#
#     def retranslateUi(self, ExitDialog):
#         _translate = QtCore.QCoreApplication.translate
#         self.setWindowTitle(_translate("ExitDialog", "Save onExit"))
#         self.label.setText(_translate("ExitDialog", "Do you want to save the code before closing?"))
#
#     def accept(self):
#         self.parent.CancelledSave = False
#         super(Ui_ExitDialog, self).accept()



class Ui_ExitDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, None)
        self.parent = parent
        self.initUI()

    def initUI(self):

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(587, 142)
        self.setMinimumSize(QtCore.QSize(587, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/window_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 30, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.YesButton = QtWidgets.QPushButton(self)
        self.YesButton.setObjectName("YesButton")
        self.horizontalLayout.addWidget(self.YesButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.NoButton = QtWidgets.QPushButton(self)
        self.NoButton.setObjectName("NoButton")
        self.horizontalLayout.addWidget(self.NoButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.CancelButton = QtWidgets.QPushButton(self)
        self.CancelButton.setObjectName("CancelButton")
        self.horizontalLayout.addWidget(self.CancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.YesButton.clicked.connect(self.OpenSave)
        self.CancelButton.clicked.connect(self.close)
        self.NoButton.clicked.connect(self.closeApplication)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def OpenSave(self):
        self.parent.CancelledSave = False
        self.close()
        self.parent.Save()

    def closeApplication(self):
        self.parent.CancelledSave = True
        self.close()
        raise SystemExit

    def closeEvent(self, QCloseEvent):
        self.close()

    def retranslateUi(self, ExitDialog):
        _translate = QtCore.QCoreApplication.translate
        ExitDialog.setWindowTitle(_translate("ExitDialog", "Save on Exit"))
        self.label.setText(_translate("ExitDialog", "Do you want to save the code before closing?"))
        self.YesButton.setText(_translate("ExitDialog", "Yes"))
        self.NoButton.setText(_translate("ExitDialog", "No"))
        self.CancelButton.setText(_translate("ExitDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExitDialog = QtWidgets.QDialog()
    ui = Ui_ExitDialog()
    ui.show()
    sys.exit(app.exec_())
