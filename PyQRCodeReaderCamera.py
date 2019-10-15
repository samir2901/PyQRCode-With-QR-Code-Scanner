from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from pyzbar.pyzbar import decode


class Ui_readFromCameraWindow(object):
    def setupUi(self, readFromCameraWindow):
        readFromCameraWindow.setObjectName("readFromCameraWindow")
        readFromCameraWindow.resize(387, 771)
        readFromCameraWindow.setMaximumSize(QtCore.QSize(387, 771))
        icon = QtGui.QIcon.fromTheme(":/appLogo/icon.png")
        readFromCameraWindow.setWindowIcon(icon)
        readFromCameraWindow.setStyleSheet("background-color: rgb(16, 100, 255);")
        self.centralwidget = QtWidgets.QWidget(readFromCameraWindow)
        self.centralwidget.setObjectName("centralwidget")



        self.titleReaderCamera = QtWidgets.QLabel(self.centralwidget)
        self.titleReaderCamera.setGeometry(QtCore.QRect(40, 20, 311, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.titleReaderCamera.setFont(font)
        self.titleReaderCamera.setStyleSheet("color: rgb(255, 255, 255);")
        self.titleReaderCamera.setObjectName("titleReaderCamera")




        self.videoSource = QtWidgets.QComboBox(self.centralwidget)
        self.videoSource.setGeometry(QtCore.QRect(190, 100, 91, 31))
        self.videoSource.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.videoSource.setObjectName("videoSource")
        self.videoSource.addItem("")
        self.videoSource.addItem("")



        self.sourcelabel = QtWidgets.QLabel(self.centralwidget)
        self.sourcelabel.setGeometry(QtCore.QRect(60, 100, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.sourcelabel.setFont(font)
        self.sourcelabel.setObjectName("sourcelabel")



        self.readCamera = QtWidgets.QPushButton(self.centralwidget)
        self.readCamera.setGeometry(QtCore.QRect(140, 160, 101, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.readCamera.setFont(font)
        self.readCamera.setStyleSheet("background-color: rgb(14, 0, 94);\n"
"color: rgb(251, 226, 255);")
        self.readCamera.setObjectName("readCamera")
        self.readCamera.clicked.connect(self.readQRCode)




        self.dataLabel = QtWidgets.QLabel(self.centralwidget)
        self.dataLabel.setGeometry(QtCore.QRect(20, 230, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.dataLabel.setFont(font)
        self.dataLabel.setObjectName("dataLabel")




        self.dataRead = QtWidgets.QTextEdit(self.centralwidget)
        self.dataRead.setGeometry(QtCore.QRect(20, 270, 351, 341))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.dataRead.setFont(font)
        self.dataRead.setStyleSheet("background-color: rgb(252, 253, 255);")
        self.dataRead.setObjectName("dataRead")
        self.dataRead.setReadOnly(True)





        self.opText = QtWidgets.QLabel(self.centralwidget)
        self.opText.setGeometry(QtCore.QRect(40, 640, 191, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.opText.setFont(font)
        self.opText.setWordWrap(True)
        self.opText.setObjectName("opText")





        self.saveasText = QtWidgets.QPushButton(self.centralwidget)
        self.saveasText.setGeometry(QtCore.QRect(260, 650, 101, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.saveasText.setFont(font)
        self.saveasText.setStyleSheet("background-color: rgb(14, 0, 94);\n"
"color: rgb(251, 226, 255);")
        self.saveasText.setObjectName("saveasText")
        self.saveasText.clicked.connect(self.saveText)





        readFromCameraWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(readFromCameraWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 387, 21))
        self.menubar.setObjectName("menubar")
        readFromCameraWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(readFromCameraWindow)
        self.statusbar.setObjectName("statusbar")
        readFromCameraWindow.setStatusBar(self.statusbar)




        self.retranslateUi(readFromCameraWindow)
        QtCore.QMetaObject.connectSlotsByName(readFromCameraWindow)

    def retranslateUi(self, readFromCameraWindow):
        _translate = QtCore.QCoreApplication.translate
        readFromCameraWindow.setWindowTitle(_translate("readFromCameraWindow", "PyQRCode Reader(Camera)"))
        self.titleReaderCamera.setText(_translate("readFromCameraWindow", "PyQRCode Reader(Camera)"))
        self.videoSource.setItemText(0, _translate("readFromCameraWindow", "0"))
        self.videoSource.setItemText(1, _translate("readFromCameraWindow", "1"))
        self.sourcelabel.setText(_translate("readFromCameraWindow", "Select Source:"))
        self.readCamera.setText(_translate("readFromCameraWindow", "Read Data"))
        self.dataLabel.setText(_translate("readFromCameraWindow", "Data:"))
        self.opText.setText(_translate("readFromCameraWindow", "If you want to save the data as a text click on this button."))
        self.saveasText.setText(_translate("readFromCameraWindow", "Save as Text"))

    def readQRCode(self):
        global x
        source = int(self.videoSource.currentText())
        try:
            cap = cv2.VideoCapture(source)
            while True:
                _, frame = cap.read()
                decoded = decode(frame)
                for obj in decoded:
                    x = obj.data
                    x = str(x)
                    frame = cv2.putText(frame, x[1:len(x)], (5,50), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,0,255), 1, cv2.LINE_AA)
                frame = cv2.putText(frame, "Press G key on KeyBoard to exit this window", (4, 400), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255), 1, cv2.LINE_AA)
                cv2.imshow("QRCode Scanner", frame)
                k = cv2.waitKey(1) & 0xFF
                if(k==ord('g')):
                    break
            cap.release()
            cv2.destroyAllWindows()             
            self.dataRead.setText(x[1:len(x)])  
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
            fileP = open(f, 'w')
            fileP.write(x[1:len(x)])
            fileP.close()
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    readFromCameraWindow = QtWidgets.QMainWindow()
    ui = Ui_readFromCameraWindow()
    ui.setupUi(readFromCameraWindow)
    readFromCameraWindow.show()
    sys.exit(app.exec_())
