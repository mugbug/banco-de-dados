
import sys
from PyQt4 import QtGui, QtCore

import design as ui
import button_listener as bt

class Application(QtGui.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.setupUi(self)
        bt.button_listener(self)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('plastique'))
    form = Application()
    form.show()
    app.exec_()