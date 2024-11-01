# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from click import clear


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(314, 434)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(-10, 5, 321, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(155, 183, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 200, 197))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(155, 183, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 200, 197))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 200, 197))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 200, 197))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.output_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.output_label.setFont(font)
        self.output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.output_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_label.setScaledContents(True)
        self.output_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output_label.setWordWrap(True)
        self.output_label.setObjectName("output_label")
        self.AC_button = QtWidgets.QPushButton(self.centralwidget)
        self.AC_button.setGeometry(QtCore.QRect(0, 60, 161, 51))
        self.AC_button.setObjectName("AC_button")
        self.DEL_button = QtWidgets.QPushButton(self.centralwidget)
        self.DEL_button.setGeometry(QtCore.QRect(150, 60, 161, 51))
        self.DEL_button.setObjectName("DEL_button")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(0, 120, 70, 61))
        self.Button_7.setObjectName("Button_7")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(80, 120, 71, 61))
        self.Button_8.setObjectName("Button_8")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(160, 120, 71, 61))
        self.Button_9.setObjectName("Button_9")
        self.plus_button = QtWidgets.QPushButton(self.centralwidget)
        self.plus_button.setGeometry(QtCore.QRect(240, 120, 71, 61))
        self.plus_button.setObjectName("plus_button")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(80, 190, 71, 61))
        self.Button_5.setObjectName("Button_5")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(0, 190, 71, 61))
        self.Button_4.setObjectName("Button_4")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(160, 190, 71, 61))
        self.Button_6.setObjectName("Button_6")
        self.minus_button = QtWidgets.QPushButton(self.centralwidget)
        self.minus_button.setGeometry(QtCore.QRect(240, 190, 71, 61))
        self.minus_button.setObjectName("minus_button")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(80, 260, 71, 61))
        self.Button_2.setObjectName("Button_2")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_0.setGeometry(QtCore.QRect(0, 330, 71, 61))
        self.Button_0.setObjectName("Button_0")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(0, 260, 71, 61))
        self.Button_1.setObjectName("Button_1")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(160, 260, 71, 61))
        self.Button_3.setObjectName("Button_3")
        self.answer_button = QtWidgets.QPushButton(self.centralwidget)
        self.answer_button.setGeometry(QtCore.QRect(160, 330, 71, 61))
        self.answer_button.setObjectName("answer_button")
        self.mul_button = QtWidgets.QPushButton(self.centralwidget)
        self.mul_button.setGeometry(QtCore.QRect(240, 260, 71, 61))
        self.mul_button.setObjectName("mul_button")
        self.div_button = QtWidgets.QPushButton(self.centralwidget)
        self.div_button.setGeometry(QtCore.QRect(240, 330, 71, 61))
        self.div_button.setObjectName("div_button")
        self.percent_button = QtWidgets.QPushButton(self.centralwidget)
        self.percent_button.setGeometry(QtCore.QRect(80, 330, 71, 61))
        self.percent_button.setObjectName("percent_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 314, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.Button_0.clicked.connect(lambda: self.press_it("0"))
        self.Button_1.clicked.connect(lambda: self.press_it("1"))
        self.Button_2.clicked.connect(lambda: self.press_it("2"))
        self.Button_3.clicked.connect(lambda: self.press_it("3"))
        self.Button_4.clicked.connect(lambda: self.press_it("4"))
        self.Button_5.clicked.connect(lambda: self.press_it("5"))
        self.Button_6.clicked.connect(lambda: self.press_it("6"))
        self.Button_7.clicked.connect(lambda: self.press_it("7"))
        self.Button_8.clicked.connect(lambda: self.press_it("8"))
        self.Button_9.clicked.connect(lambda: self.press_it("9"))
        self.plus_button.clicked.connect(lambda: self.press_it("+"))
        self.minus_button.clicked.connect(lambda: self.press_it("-"))
        self.mul_button.clicked.connect(lambda: self.press_it("*"))
        self.div_button.clicked.connect(lambda: self.press_it("/"))
        self.percent_button.clicked.connect(lambda: self.press_it("%"))

        self.AC_button.clicked.connect(self.clear)
        
        self.DEL_button.clicked.connect(self.Del)
        
        self.answer_button.clicked.connect(self.calculate)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "simple Calculator"))
        self.output_label.setText(_translate("MainWindow", "0"))
        self.AC_button.setText(_translate("MainWindow", "AC"))
        self.DEL_button.setText(_translate("MainWindow", "DEL"))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.plus_button.setText(_translate("MainWindow", "+"))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.minus_button.setText(_translate("MainWindow", "-"))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.answer_button.setText(_translate("MainWindow", "="))
        self.mul_button.setText(_translate("MainWindow", "*"))
        self.div_button.setText(_translate("MainWindow", "/"))
        self.percent_button.setText(_translate("MainWindow", "%"))
    
    answer_flag = None
    
    def press_it(self,value):
        current_text = self.output_label.text()
        
        # Check if the current text is "0", reset it if necessary
        if current_text == "0" or current_text == "ERROR" or self.answer_flag == 1:
            self.output_label.setText(value)
            self.answer_flag = 0
        else:
            # Append the button's text to the current text
            self.output_label.setText(current_text + value)

        
    
    def clear(self):
        self.output_label.setText("0")
    
    def Del(self):
        current_text = self.output_label.text()
        if len(current_text) == 1:
            self.output_label.setText("0")
        else:
            self.output_label.setText(current_text[:-1])
        
    def calculate(self):
        try: 
            screen = self.output_label.text()
            answer = str(eval(screen))
            self.output_label.setText(answer)
        except:
            self.output_label.setText("ERROR")
        self.answer_flag = 1
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())