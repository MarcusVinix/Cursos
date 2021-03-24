from PyQt4 import QtGui, QtCore
import sys
class Main(QtGui.QWidget):
    def __init__(self, master=None):
        QtGui.QWidget.__init__(self, master)
        self.setGeometry(400, 300, 250, 250)

        self.setWindowTitle("Teste")
        labelTeste = QtGui.QLabel("Testando", self)
        labelTeste.setGeometry(20, 20, 100, 10)

        botao = QtGui.QPushButton("OK", self)
        botao.setGeometry(50, 50, 50, 30)

app = QtGui.QApplication(sys.argv)
programa = Main()
programa.show()

sys.exit(app.exec_())