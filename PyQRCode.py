from PyQt5 import QtCore, QtGui, QtWidgets
from PyQRCodeAbout import Ui_AboutWindow
from PyQRCodeHelp import Ui_HelpWindow
from PyQRCodeGenerator import Ui_generatorWindow
from PyQRCodeReaderCamera import Ui_readFromCameraWindow
from PyQRCodeReaderImage import Ui_readFromImageWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 259)
        MainWindow.setMaximumSize(QtCore.QSize(705, 259))
        icon = QtGui.QIcon.fromTheme(":/appLogo/icon.png")
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(52, 1, 255);\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleApp = QtWidgets.QLabel(self.centralwidget)
        self.titleApp.setGeometry(QtCore.QRect(280, 0, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titleApp.setFont(font)
        self.titleApp.setStyleSheet("background-color: rgb(52, 1, 255);\n"
"color: rgb(239, 219, 255);")
        self.titleApp.setObjectName("titleApp")



        self.generateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.generateBtn.setGeometry(QtCore.QRect(90, 100, 131, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.generateBtn.setFont(font)
        self.generateBtn.setStyleSheet("background-color: rgb(14, 0, 94);\n"
"color: rgb(251, 226, 255);")
        self.generateBtn.setObjectName("generateBtn")
        self.generateBtn.clicked.connect(self.generatorWindowOpen)




        self.readfromImageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.readfromImageBtn.setGeometry(QtCore.QRect(290, 100, 131, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.readfromImageBtn.setFont(font)
        self.readfromImageBtn.setAutoFillBackground(False)
        self.readfromImageBtn.setStyleSheet("background-color: rgb(14, 0, 94);\n"
"color: rgb(251, 226, 255);")
        self.readfromImageBtn.setObjectName("readfromImageBtn")
        self.readfromImageBtn.clicked.connect(self.readerImageWindowOpen)




        self.readCameraBtn = QtWidgets.QPushButton(self.centralwidget)
        self.readCameraBtn.setGeometry(QtCore.QRect(510, 100, 131, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.readCameraBtn.setFont(font)
        self.readCameraBtn.setStyleSheet("background-color: rgb(14, 0, 94);\n"
"color: rgb(251, 226, 255);")
        self.readCameraBtn.setObjectName("readCameraBtn")
        self.readCameraBtn.clicked.connect(self.readerCameraWindowOpen)





        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.menubar.setObjectName("menubar")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuView.addAction(self.actionHelp)
        self.menuView.addAction(self.actionAbout)
        self.menubar.addAction(self.menuView.menuAction())
        self.actionAbout.triggered.connect(self.aboutWindowOpen)
        self.actionHelp.triggered.connect(self.helpWindowOpen)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQRCode"))
        self.titleApp.setText(_translate("MainWindow", "PyQRCode"))
        self.generateBtn.setText(_translate("MainWindow", "Generate QR Code"))
        self.readfromImageBtn.setText(_translate("MainWindow", "Read From Image"))
        self.readCameraBtn.setText(_translate("MainWindow", "Read Using Camera"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def helpWindowOpen(self):
        self.window = QtWidgets.QMainWindow()
        self.helpUI = Ui_HelpWindow()
        self.helpUI.setupUi(self.window)
        self.window.show()
        print("Help Window is Opened")

    def aboutWindowOpen(self):
        self.window = QtWidgets.QMainWindow()
        self.aboutUI = Ui_AboutWindow()
        self.aboutUI.setupUi(self.window)
        self.window.show()
        print("About Window is Opened")


    def generatorWindowOpen(self):
        self.window = QtWidgets.QMainWindow()
        self.generatorUI = Ui_generatorWindow()
        self.generatorUI.setupUi(self.window)
        self.window.show()
        print("Generator Window is Opened")

    def readerImageWindowOpen(self):
        self.window = QtWidgets.QMainWindow()
        self.readerImageUI = Ui_readFromImageWindow()
        self.readerImageUI.setupUi(self.window)
        self.window.show()
        print("Read From Image Window is Opened")

    def readerCameraWindowOpen(self):
        self.window = QtWidgets.QMainWindow()
        self.readerCameraUI = Ui_readFromCameraWindow()
        self.readerCameraUI.setupUi(self.window)
        self.window.show()
        print("Read From Camera Window is opened")



    
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
