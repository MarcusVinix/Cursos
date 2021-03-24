import sys
from PyQt4 import QtGui, QtCore
from pessoa import Ui_Dialog
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.mostra)
    
    def mostra(self):
        print("Testando")
        self.ui.lineEdit_2.setText("Testando")

app = QtGui.QApplication(sys.argv)
programa = Main()
programa.show()
sys.exit(app.exec_())
