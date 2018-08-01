import sys
from PyQt5.QtWidgets import QWidget,  QAction, QMessageBox, QPushButton, QLineEdit, QInputDialog, QApplication, QFileDialog, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'DICOM TO BIDS CONVERTER'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Here is the button for the Study/Experiment Name
        self.studyName = QLineEdit(self)
        self.studyName.move(20,20)
        self.studyName.resize(200,20)
        self.name_btn = QPushButton("Enter Experiment Name", self)
        self.name_btn.move(250, 20)
        self.name_btn.clicked.connect(self.getStudyName)


        # Menu, or "combo box" for multi-session parameter
        self.multiSess = QComboBox(self)
        self.multiSess.addItem("Yes")
        self.multiSess.addItem("No")
        self.multiSess.move(20, 60)
        self.multiSess.activated.connect(self.multiSession)
        #studyname_btn = QPushButton('Experiment Name', self)
        #studyname_btn.move(100,70)
        #studyname_btn.clicked.connect(self.on_click)


        self.inputdir_btn = QPushButton("INPUT DIRECTORY", self)
        self.inputdir_btn.move(20, 100)
        self.inputdir_btn.clicked.connect(self.getInputDir)

#        self.le = QLineEdit(self)
#        self.le.move(130, 22)

        self.show()



    def getInputDir(self):
        #self.dlg = QFileDialog()
        #self.dlg.setFileMode(QFileDialog.Directory)

        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
        self.setPixmap(QPixmap(fname))
        #if dlg.exec_():
        #    filenames = dlg.selectedFiles()
    def pick_new():
        dialog = QtGui.QFileDialog()
        folder_path = dialog.getExistingDirectory(None, "Select Folder")
        return folder_path

    @pyqtSlot()
    def multiSession(self):
        print("CURRENT CHOICE: ", self.multiSess.currentText())

    def getStudyName(self):
        STUDYNAME = self.studyName.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + STUDYNAME, QMessageBox.Ok, QMessageBox.Ok)
        self.studyName.setText("")

    def on_click(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
            'Enter the study name:')
        if ok:
            self.le.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
