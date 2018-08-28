import sys
from PyQt5.QtWidgets import QWidget, QLabel,  QAction, QMessageBox, QPushButton, QLineEdit, QInputDialog, QApplication, QFileDialog, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'DICOM TO BIDS CONVERTER'
        self.left = 5
        self.top = 5
        self.width = 550
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.guiTitle = QLabel("DICOM to BIDS Converter", self)
        self.guiTitle.move(20, 50)
        # Here is the button for the Study/Experiment Name
        self.studyName = QLineEdit(self)
        self.studyName.move(20,100)
        self.studyName.resize(200,20)
        self.name_btn = QPushButton("Enter Experiment Name", self)
        self.name_btn.move(230, 95)
        self.name_btn.clicked.connect(self.getStudyName)

        self.textA = QLabel("Multiple sessions:", self)
        self.textA.move(20, 140)
        # Menu, or "combo box" for multi-session parameter
        self.multiSess = QComboBox(self)
        self.multiSess.addItem("No")
        self.multiSess.addItem("Yes")
        self.multiSess.move(130, 134)
        self.multiSess.activated.connect(self.multiSession)
        #studyname_btn = QPushButton('Experiment Name', self)
        #studyname_btn.move(100,70)
        #studyname_btn.clicked.connect(self.on_click)


        self.inputdir_btn = QPushButton("INPUT DIRECTORY", self)
        self.inputdir_btn.move(20, 170)
        self.inputdir_btn.clicked.connect(self.getInputDir)

        self.outputdir_btn = QPushButton("OUTPUT DIRECTORY", self)
        self.outputdir_btn.move(20, 200)
        self.outputdir_btn.clicked.connect(self.getOutputDir)

#        self.le = QLineEdit(self)
#        self.le.move(130, 22)

        self.dicomPath = QLineEdit(self)
        self.dicomPath.move(20,240)
        self.dicomPath.resize(200,20)
        self.dicom_btn = QPushButton("Enter Path to Dicoms", self)
        self.dicom_btn.move(230, 235)
        self.dicom_btn.clicked.connect(self.getDicomPath)


        self.startProcess_btn = QPushButton("START CONVERSION", self)
        self.startProcess_btn.move(15, 290)
        self.startProcess_btn.connect(self.startConversion)

        self.show()


    def getOutputDir(self):
        OUTPUTDIR = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        print("---------------------> OUTPUT DIRECTORY: ", OUTPUTDIR)

        #self.setPixmap(QPixmap(OUTPUTDIR))
    def getInputDir(self):
        INPUTDIR = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        print("---------------------> INPUT DIRECTORY: ", INPUTDIR)

    @pyqtSlot()
    def multiSession(self):
        print("CURRENT CHOICE: ", self.multiSess.currentText())

    def getStudyName(self):
        STUDYNAME = self.studyName.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + STUDYNAME, QMessageBox.Ok, QMessageBox.Ok)
        self.studyName.setText("")
    def getDicomPath(self):
        DICOMPATH = self.dicomPath.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + DICOMPATH, QMessageBox.Ok, QMessageBox.Ok)
        self.dicomPath.setText("")
    def startConversion(self):
        if 


"""
    def on_click(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
            'Enter the study name:')
        if ok:
            self.le.setText(str(text))
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
