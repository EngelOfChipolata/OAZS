# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui.ui'
#
# Created: Thu Nov  6 12:29:44 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Ui(object):
    def setupUi(self, Ui):
        Ui.setObjectName(_fromUtf8("Ui"))
        Ui.resize(550, 484)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Images/flight_on_1600x1200.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Ui.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Ui)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.infos = QtGui.QLabel(Ui)
        self.infos.setEnabled(True)
        self.infos.setMinimumSize(QtCore.QSize(0, 30))
        self.infos.setMaximumSize(QtCore.QSize(16777215, 30))
        self.infos.setStyleSheet(_fromUtf8("background-color: rgb(227, 227, 227);"))
        self.infos.setText(_fromUtf8(""))
        self.infos.setAlignment(QtCore.Qt.AlignCenter)
        self.infos.setObjectName(_fromUtf8("infos"))
        self.verticalLayout_2.addWidget(self.infos)
        self.scrollArea = QtGui.QScrollArea(Ui)
        self.scrollArea.setMinimumSize(QtCore.QSize(480, 260))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollbar=self.scrollArea.verticalScrollBar()
        self.scrollbar.rangeChanged.connect(self.movebottom)
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 528, 399))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))

        self.gridLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.terminal = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.terminal.setMinimumSize(QtCore.QSize(474, 250))
        self.terminal.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.terminal.setFrameShape(QtGui.QFrame.StyledPanel)
        self.terminal.setFrameShadow(QtGui.QFrame.Sunken)
        self.terminal.setTextFormat(QtCore.Qt.RichText)
        self.terminal.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.terminal.setWordWrap(True)
        self.terminal.setObjectName(_fromUtf8("terminal"))
        self.gridLayout.addWidget(self.terminal, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.playerinput = QtGui.QLineEdit(Ui)
        self.playerinput.setMinimumSize(QtCore.QSize(100, 27))
        self.playerinput.setMaximumSize(QtCore.QSize(16777215, 27))
        self.playerinput.setObjectName(_fromUtf8("playerinput"))
        self.verticalLayout_3.addWidget(self.playerinput)
        self.retranslateUi(Ui)
        QtCore.QMetaObject.connectSlotsByName(Ui)

    def retranslateUi(self, Ui):
        Ui.setWindowTitle(_translate("Ui", "Zork like", None))
        self.terminal.setText(_translate("Ui", "<html><head/><body><p><br/></p></body></html>", None))


    def movebottom(self, a, b):
        self.scrollbar.setValue(b)