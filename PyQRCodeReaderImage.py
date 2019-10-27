from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from pyzbar.pyzbar import decode


class Ui_readFromImageWindow(object):
    def setupUi(self, readFromImageWindow):
        readFromImageWindow.setObjectName("readFromImageWindow")
        readFromImageWindow.resize(391, 722)
        readFromImageWindow.setMaximumSize(QtCore.QSize(391, 722))
        icon = QtGui.QIcon.fromTheme(":/appLogo/icon.png")
        readFromImageWindow.setWindowIcon(icon)
        readFromImageWindow.setStyleSheet("background-color: rgb(16, 100, 255);")
        self.centralwidget = QtWidgets.QWidget(readFromImageWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.dataRead = QtWidgets.QTextEdit(self.centralwidget)
        self.dataRead.setGeometry(QtCore.QRect(20, 230, 351, 341))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.dataRead.setFont(font)
        self.dataRead.setStyleSheet("background-color: rgb(252, 253, 255);")
        self.dataRead.setObjectName("dataRead")
        self.dataRead.setReadOnly(True)


        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(40, 120, 101, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.browse.setFont(font)
        self.browse.setStyleSheet("background-color: rgb(14, 0, 94);\n"
"color: rgb(251, 226, 255);")
        self.browse.setObjectName("browse")
        self.browse.clicked.connect(self.browseFileName)


        self.titleReaderImage = QtWidgets.QLabel(self.centralwidget)
        self.titleReaderImage.setGeometry(QtCore.QRect(50, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.titleReaderImage.setFont(font)
        self.titleReaderImage.setStyleSheet("color: rgb(255, 255, 255);")
        self.titleReaderImage.setObjectName("titleReaderImage")



        self.openLabel = QtWidgets.QLabel(self.centralwidget)
        self.openLabel.setGeometry(QtCore.QRect(20, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.openLabel.setFont(font)
        self.openLabel.setObjectName("openLabel")



        self.readImage = QtWidgets.QPushButton(self.centralwidget)
        self.readImage.setGeometry(QtCore.QRect(250, 120, 101, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.readImage.setFont(font)
        self.readImage.setStyleSheet("background-color: rgb(14, 0, 94);\n"
"color: rgb(251, 226, 255);")
        self.readImage.setObjectName("readImage")
        self.readImage.clicked.connect(self.readQRCode)



        self.dataLabel = QtWidgets.QLabel(self.centralwidget)
        self.dataLabel.setGeometry(QtCore.QRect(20, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.dataLabel.setFont(font)
        self.dataLabel.setObjectName("dataLabel")



        self.saveasText = QtWidgets.QPushButton(self.centralwidget)
        self.saveasText.setGeometry(QtCore.QRect(250, 610, 101, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.saveasText.setFont(font)
        self.saveasText.setStyleSheet("background-color: rgb(14, 0, 94);\n"
"color: rgb(251, 226, 255);")
        self.saveasText.setObjectName("saveasText")
        self.saveasText.clicked.connect(self.saveText)


        self.opText = QtWidgets.QLabel(self.centralwidget)
        self.opText.setGeometry(QtCore.QRect(30, 600, 191, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.opText.setFont(font)
        self.opText.setWordWrap(True)
        self.opText.setObjectName("opText")



        readFromImageWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(readFromImageWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 21))
        self.menubar.setObjectName("menubar")
        readFromImageWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(readFromImageWindow)
        self.statusbar.setObjectName("statusbar")
        readFromImageWindow.setStatusBar(self.statusbar)

        self.retranslateUi(readFromImageWindow)
        QtCore.QMetaObject.connectSlotsByName(readFromImageWindow)

    def retranslateUi(self, readFromImageWindow):
        _translate = QtCore.QCoreApplication.translate
        readFromImageWindow.setWindowTitle(_translate("readFromImageWindow", "PyQRCode Reader(Image)"))
        self.browse.setText(_translate("readFromImageWindow", "Browse"))
        self.titleReaderImage.setText(_translate("readFromImageWindow", "PyQRCode Reader(Image)"))
        self.openLabel.setText(_translate("readFromImageWindow", "Open Image"))
        self.readImage.setText(_translate("readFromImageWindow", "Read Data"))
        self.dataLabel.setText(_translate("readFromImageWindow", "Data:"))
        self.saveasText.setText(_translate("readFromImageWindow", "Save as Text"))
        self.opText.setText(_translate("readFromImageWindow", "If you want to save the data as a text click on this button."))


    def browseFileName(self):
        global filename
        filter = "*.png"
        fm = QtWidgets.QFileDialog.getOpenFileName(None, "Open File", ".", filter)
        filename = fm[0]
        print(filename)
        print("Browse Button Pressed.")

    
    def readQRCode(self):
        global d
        try:
            image = cv2.imread(filename)
            decoded = decode(image)
            d = str(decoded[0].data)
            d = d[1:len(d)]
            self.dataRead.setText(d)
        except:
            msgError = QtWidgets.QMessageBox()
            msgError.setIcon(QtWidgets.QMessageBox.Critical)
            msgError.setWindowTitle("Error")
            msgError.setText("Oops!! Error")
            msgError.exec_()             

    def saveText(self):
        try:
            fp = QtWidgets.QFileDialog.getSaveFileName(None, "Save File As", ".", "*.txt")
            f = fp[0]
            x = open(f, 'w')
            x.write(d)
            x.close()
            msgSaved = QtWidgets.QMessageBox()
            msgSaved.setIcon(QtWidgets.QMessageBox.Information)
            msgSaved.setWindowTitle("Saved")
            msgSaved.setText("Data Saved as text")
            msgSaved.exec_() 
        except:
            msgError = QtWidgets.QMessageBox()
            msgError.setIcon(QtWidgets.QMessageBox.Critical)
            msgError.setWindowTitle("Error")
            msgError.setText("Oops!! Error")
            msgError.exec_() 
    
import logo_rc
