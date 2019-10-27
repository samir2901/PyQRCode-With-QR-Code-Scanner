from PyQt5 import QtCore, QtGui, QtWidgets
import qrcode

class Ui_generatorWindow(object):
    def setupUi(self, generatorWindow):
        generatorWindow.setObjectName("generatorWindow")
        generatorWindow.resize(386, 570)
        generatorWindow.setMaximumSize(QtCore.QSize(386, 570))
        icon = QtGui.QIcon.fromTheme(":/appLogo/icon.png")
        generatorWindow.setWindowIcon(icon)
        generatorWindow.setStyleSheet("background-color: rgb(16, 100, 255);")
        self.centralwidget = QtWidgets.QWidget(generatorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleGenerator = QtWidgets.QLabel(self.centralwidget)
        self.titleGenerator.setGeometry(QtCore.QRect(80, 10, 241, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.titleGenerator.setFont(font)
        self.titleGenerator.setStyleSheet("color: rgb(255, 255, 255);")
        self.titleGenerator.setObjectName("titleGenerator")


        self.dataLabel = QtWidgets.QLabel(self.centralwidget)
        self.dataLabel.setGeometry(QtCore.QRect(20, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.dataLabel.setFont(font)
        self.dataLabel.setObjectName("dataLabel")


        self.dataEntry = QtWidgets.QTextEdit(self.centralwidget)
        self.dataEntry.setGeometry(QtCore.QRect(20, 100, 351, 321))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.dataEntry.setFont(font)
        self.dataEntry.setStyleSheet("background-color: rgb(252, 253, 255);")
        self.dataEntry.setObjectName("dataEntry")


        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(50, 450, 101, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.browse.setFont(font)
        self.browse.setStyleSheet("background-color: rgb(14, 0, 94);\n"
"color: rgb(251, 226, 255);")
        self.browse.setObjectName("browse")
        self.browse.clicked.connect(self.browseFileName)

        
        self.saveandGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.saveandGenerate.setGeometry(QtCore.QRect(230, 450, 101, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.saveandGenerate.setFont(font)
        self.saveandGenerate.setStyleSheet("background-color: rgb(14, 0, 94);\n"
"color: rgb(251, 226, 255);")
        self.saveandGenerate.setObjectName("saveandGenerate")
        self.saveandGenerate.clicked.connect(self.makeQRCode)



        generatorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(generatorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 386, 21))
        self.menubar.setObjectName("menubar")
        generatorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(generatorWindow)
        self.statusbar.setObjectName("statusbar")
        generatorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(generatorWindow)
        QtCore.QMetaObject.connectSlotsByName(generatorWindow)

    def retranslateUi(self, generatorWindow):
        _translate = QtCore.QCoreApplication.translate
        generatorWindow.setWindowTitle(_translate("generatorWindow", "PyQRCode Generator"))
        self.titleGenerator.setText(_translate("generatorWindow", "PyQRCode Generator"))
        self.dataLabel.setText(_translate("generatorWindow", "Enter the data"))
        self.browse.setText(_translate("generatorWindow", "Browse"))
        self.saveandGenerate.setText(_translate("generatorWindow", "Save"))

    def browseFileName(self):
        global filename
        fm = QtWidgets.QFileDialog.getSaveFileName(None, "Save File As",".","*.png")
        filename = fm[0]
        print(filename)
        print("Browse Button Pressed.")

    def makeQRCode(self):
        try:
            txt = self.dataEntry.toPlainText()
            qr = qrcode.QRCode(version=1,box_size=10,border=5)
            qr.add_data(txt)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(filename)
            print("File Converted")            
            msgDone = QtWidgets.QMessageBox()
            msgDone.setIcon(QtWidgets.QMessageBox.Information)
            msgDone.setWindowTitle("Done")
            msgDone.setText("QRCode is Generated.")
            msgDone.exec_()
        except:
            msgError = QtWidgets.QMessageBox()
            msgError.setIcon(QtWidgets.QMessageBox.Critical)
            msgError.setWindowTitle("Error")
            msgError.setText("Oops!! Error")
            msgError.exec_()
        
            
import logo_rc

