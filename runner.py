
import sys
from PyQt4 import QtGui, QtCore

import design as ui
import button_listener as bt

class Application(QtGui.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.setupUi(self)
        self.ui_config()
        bt.button_listener(self)

    def ui_config(self):
        # inicia com tela de cadastro de aluno
        self.toolBox.setCurrentIndex(0)
        self.aluno_widget.setCurrentIndex(0)
        self.aluno_btn_create.setEnabled(False)
        self.aluno_btn_edit.setEnabled(False)
        self.aluno_btn_search.setEnabled(True)
        self.aluno_btn_list.setEnabled(True)
        self.aluno_btn_remove.setEnabled(False)
        self.aluno_btn_nota.setEnabled(True)
        # init tela de curso
        self.curso_widget.setCurrentIndex(1)
        self.curso_btn_create.setEnabled(True)
        self.curso_btn_edit.setEnabled(False)
        self.curso_btn_search.setEnabled(False)
        self.curso_btn_list.setEnabled(False)
        self.curso_btn_remove.setEnabled(False)
        # init tela de materia
        self.materia_widget.setCurrentIndex(1)
        self.materia_btn_create.setEnabled(True)
        self.materia_btn_edit.setEnabled(False)
        self.materia_btn_search.setEnabled(False)
        self.materia_btn_list.setEnabled(False)
        self.materia_btn_remove.setEnabled(False)
        # init notas
        self.aluno_input_np2.setEnabled(False)
        self.aluno_input_np3.setEnabled(False)
        self.aluno_input_nf.setEnabled(False)
        self.aluno_input_situacao.setEnabled(False)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('plastique'))
    form = Application()
    form.show()
    app.exec_()