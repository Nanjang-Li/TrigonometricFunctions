# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculatori.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

WIDTH = (75 + 2 * 2) * 4 + 3
HEIGHT = (50 + 2 * 2) * 5 + 3 + 70
button_style = "QPushButton{" \
               "background-color:rgb(0,0,0);" \
               "border:1px solid rgb(216,216,216);" \
               "color:rgb(255,255,255);" \
               "width:75px;" \
               "height:50px;" \
               "font:bold 16pt \"Arial\";" \
               "}" \
               "QPushButton:hover{" \
               "background-color:rgba(0,0,0,0);" \
               "}"


class Button(QtWidgets.QPushButton):
    def __init__(self, parent):
        super(Button, self).__init__(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
        self.setStyleSheet(button_style)


class NumberButton(Button):
    def __init__(self, parent=None):
        super(NumberButton, self).__init__(parent)


class TrigonometricButton(Button):
    def __init__(self, parent=None):
        super(TrigonometricButton, self).__init__(parent)


class FunctionButton(Button):
    def __init__(self, parent=None):
        super(FunctionButton, self).__init__(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding))


class UiMainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(WIDTH, HEIGHT)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, WIDTH, HEIGHT))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setStyleSheet("background-color:rgb(31,31,31);")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSpacing(2)
        # 输入显示框
        self.display_box = QtWidgets.QLabel(self.gridLayoutWidget)
        self.display_box.setObjectName("display_box")
        self.display_box.setFixedHeight(70)
        self.display_box.setText("0")
        self.display_box.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.display_box.setStyleSheet("color:rgb(255,255,255);"
                                       "font:bold 24pt \"Arial\";"
                                       )
        self.display_box.setContentsMargins(0, 0, 5, 3)
        self.gridLayout.addWidget(self.display_box, 0, 0, 1, 4)
        # 三角函数按钮
        self.sin_button = TrigonometricButton(self.gridLayoutWidget)
        self.sin_button.setObjectName("sin_button")
        self.gridLayout.addWidget(self.sin_button, 1, 0, 1, 1)
        self.cos_button = TrigonometricButton(self.gridLayoutWidget)
        self.cos_button.setObjectName("cos_button")
        self.gridLayout.addWidget(self.cos_button, 1, 1, 1, 1)
        self.arctan_button = TrigonometricButton(self.gridLayoutWidget)
        self.arctan_button.setObjectName("arctan_button")
        self.gridLayout.addWidget(self.arctan_button, 1, 2, 1, 1)
        self.arcsin_button = TrigonometricButton(self.gridLayoutWidget)
        self.arcsin_button.setObjectName("arcsin_button")
        self.gridLayout.addWidget(self.arcsin_button, 1, 3, 1, 1)
        # 数字按钮0-9
        self.number_0_button = NumberButton(self.gridLayoutWidget)
        self.number_0_button.setObjectName("number_0_button")
        self.number_0_button.setSizePolicy(
            QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed))
        self.gridLayout.addWidget(self.number_0_button, 5, 0, 1, 2)
        self.number_1_button = NumberButton(self.gridLayoutWidget)
        self.number_1_button.setObjectName("number_1_button")
        self.gridLayout.addWidget(self.number_1_button, 4, 0, 1, 1)
        self.number_2_button = NumberButton(self.gridLayoutWidget)
        self.number_2_button.setObjectName("number_2_button")
        self.gridLayout.addWidget(self.number_2_button, 4, 1, 1, 1)
        self.number_3_button = NumberButton(self.gridLayoutWidget)
        self.number_3_button.setObjectName("number_3_button")
        self.gridLayout.addWidget(self.number_3_button, 4, 2, 1, 1)
        self.number_4_button = NumberButton(self.gridLayoutWidget)
        self.number_4_button.setObjectName("number_4_button")
        self.gridLayout.addWidget(self.number_4_button, 3, 0, 1, 1)
        self.number_5_button = NumberButton(self.gridLayoutWidget)
        self.number_5_button.setObjectName("number_5_button")
        self.gridLayout.addWidget(self.number_5_button, 3, 1, 1, 1)
        self.number_6_button = NumberButton(self.gridLayoutWidget)
        self.number_6_button.setObjectName("number_6_button")
        self.gridLayout.addWidget(self.number_6_button, 3, 2, 1, 1)
        self.number_7_button = NumberButton(self.gridLayoutWidget)
        self.number_7_button.setObjectName("number_7_button")
        self.gridLayout.addWidget(self.number_7_button, 2, 0, 1, 1)
        self.number_8_button = NumberButton(self.gridLayoutWidget)
        self.number_8_button.setObjectName("number_8_button")
        self.gridLayout.addWidget(self.number_8_button, 2, 1, 1, 1)
        self.number_9_button = NumberButton(self.gridLayoutWidget)
        self.number_9_button.setObjectName("number_9_button")
        self.gridLayout.addWidget(self.number_9_button, 2, 2, 1, 1)
        # 小数点
        self.dot_button = Button(self.gridLayoutWidget)
        self.dot_button.setObjectName("dot_button")
        self.gridLayout.addWidget(self.dot_button, 5, 2, 1, 1)
        # 复位按钮
        self.reset_button = FunctionButton(self.gridLayoutWidget)
        self.reset_button.setObjectName("reset_button")
        self.gridLayout.addWidget(self.reset_button, 2, 3, 2, 1)
        # 清除按钮
        self.del_button = FunctionButton(self.gridLayoutWidget)
        self.del_button.setObjectName("del_button")
        self.gridLayout.addWidget(self.del_button, 4, 3, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.number_5_button.setText(_translate("MainWindow", "5"))
        self.number_2_button.setText(_translate("MainWindow", "2"))
        self.arcsin_button.setText(_translate("MainWindow", "arcsin"))
        self.reset_button.setText(_translate("MainWindow", "C"))
        self.sin_button.setText(_translate("MainWindow", "sin"))
        self.number_8_button.setText(_translate("MainWindow", "8"))
        self.dot_button.setText(_translate("MainWindow", "."))
        self.number_6_button.setText(_translate("MainWindow", "6"))
        self.number_0_button.setText(_translate("MainWindow", "0"))
        self.cos_button.setText(_translate("MainWindow", "cos"))
        self.number_9_button.setText(_translate("MainWindow", "9"))
        self.arctan_button.setText(_translate("MainWindow", "arctan"))
        self.number_7_button.setText(_translate("MainWindow", "7"))
        self.number_1_button.setText(_translate("MainWindow", "1"))
        self.number_3_button.setText(_translate("MainWindow", "3"))
        self.number_4_button.setText(_translate("MainWindow", "4"))
        self.del_button.setText(_translate("MainWindow", "del"))
