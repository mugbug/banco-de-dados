
from PyQt4.QtGui import QMessageBox
from PyQt4 import QtGui, QtCore

import button_features as bf

def button_listener(app):
    # Aluno
    app.aluno_btn_create.clicked.connect(lambda: switch_widget(app, 1, 0))
    app.aluno_btn_edit.clicked.connect(lambda: bf.edit_aluno(app))
    app.aluno_btn_search.clicked.connect(lambda: switch_widget(app, 1, 2))
    app.aluno_btn_list.clicked.connect(lambda: switch_widget(app, 1, 2))
    app.aluno_btn_remove.clicked.connect(lambda: bf.remove_aluno(app))
    app.aluno_btn_nota.clicked.connect(lambda: switch_widget(app, 1, 1))

    app.aluno_submeter.clicked.connect(lambda: bf.create_aluno(app))
    app.aluno_submeter_nota.clicked.connect(lambda: bf.nota_aluno(app))
    # Curso
    app.curso_btn_create.clicked.connect(lambda: switch_widget(app, 2, 0))
    app.curso_btn_edit.clicked.connect(lambda: bf.edit_curso(app))
    app.curso_btn_search.clicked.connect(lambda: switch_widget(app, 2, 1))
    app.curso_btn_list.clicked.connect(lambda: switch_widget(app, 2, 1))
    app.curso_btn_remove.clicked.connect(lambda: bf.remove_curso(app))

    app.curso_submeter.clicked.connect(lambda: bf.create_curso(app))

    # Materia
    app.materia_btn_create.clicked.connect(lambda: switch_widget(app, 3, 0))
    app.materia_btn_edit.clicked.connect(lambda: bf.edit_materia(app))
    app.materia_btn_search.clicked.connect(lambda: switch_widget(app, 3, 1))
    app.materia_btn_list.clicked.connect(lambda: switch_widget(app, 3, 1))
    app.materia_btn_remove.clicked.connect(lambda: bf.remove_materia(app))

    app.materia_submeter.clicked.connect(lambda: bf.create_materia(app))

def switch_widget(app, widget_id, index):
    # widget_id:
    #   1: Aluno
    #   2: Curso
    #   3: Materia
    if widget_id == 1:
<<<<<<< HEAD
        if index == 0: # tela de cadastro/edicao
            app.aluno_btn_create.setEnabled(False)
            app.aluno_btn_edit.setEnabled(False)
            app.aluno_btn_search.setEnabled(True)
            app.aluno_btn_list.setEnabled(True)
            app.aluno_btn_remove.setEnabled(False)
            app.aluno_btn_nota.setEnabled(True)
        if index == 1: # tela de notas
            app.aluno_btn_create.setEnabled(True)
            app.aluno_btn_edit.setEnabled(False)
            app.aluno_btn_search.setEnabled(True)
            app.aluno_btn_list.setEnabled(True)
            app.aluno_btn_remove.setEnabled(False)
            app.aluno_btn_nota.setEnabled(False)
        if index == 2: # tela de consulta
            app.aluno_btn_create.setEnabled(True)
            app.aluno_btn_edit.setEnabled(True)
            app.aluno_btn_search.setEnabled(False)
            app.aluno_btn_list.setEnabled(False)
            app.aluno_btn_remove.setEnabled(True)
            app.aluno_btn_nota.setEnabled(True)
        app.aluno_widget.setCurrentIndex(index)

    if widget_id == 2:
        if index == 0: # tela de cadastro/edicao
            app.curso_btn_create.setEnabled(False)
            app.curso_btn_edit.setEnabled(False)
            app.curso_btn_search.setEnabled(True)
            app.curso_btn_list.setEnabled(True)
            app.curso_btn_remove.setEnabled(False)
        if index == 1: # tela de consulta
            app.curso_btn_create.setEnabled(True)
            app.curso_btn_edit.setEnabled(True)
            app.curso_btn_search.setEnabled(False)
            app.curso_btn_list.setEnabled(False)
            app.curso_btn_remove.setEnabled(True)
        app.curso_widget.setCurrentIndex(index)

    if widget_id == 3:
        if index == 0: # tela de cadastro/edicao
            app.materia_btn_create.setEnabled(False)
            app.materia_btn_edit.setEnabled(False)
            app.materia_btn_search.setEnabled(True)
            app.materia_btn_list.setEnabled(True)
            app.materia_btn_remove.setEnabled(False)
        if index == 1: # tela de consulta
            app.materia_btn_create.setEnabled(True)
            app.materia_btn_edit.setEnabled(True)
            app.materia_btn_search.setEnabled(False)
            app.materia_btn_list.setEnabled(False)
            app.materia_btn_remove.setEnabled(True)
        app.materia_widget.setCurrentIndex(index)