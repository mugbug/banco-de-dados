from PyQt4 import QtGui, QtCore

def button_listener(app):
    # Aluno
    app.aluno_btn_create.clicked.connect(lambda: switch_widget(app, 1, 0))
    app.aluno_btn_edit.clicked.connect(lambda: switch_widget(app, 1, 0))
    app.aluno_btn_search.clicked.connect(lambda: switch_widget(app, 1, 2))
    app.aluno_btn_list.clicked.connect(lambda: switch_widget(app, 1, 2))
    app.aluno_btn_remove.clicked.connect(lambda: switch_widget(app, 1, 2))
    app.aluno_btn_nota.clicked.connect(lambda: switch_widget(app, 1, 1))

    # Curso
    app.curso_btn_create.clicked.connect(lambda: switch_widget(app, 2, 0))
    app.curso_btn_edit.clicked.connect(lambda: switch_widget(app, 2, 0))
    app.curso_btn_search.clicked.connect(lambda: switch_widget(app, 2, 1))
    app.curso_btn_list.clicked.connect(lambda: switch_widget(app, 2, 1))
    app.curso_btn_remove.clicked.connect(lambda: switch_widget(app, 2, 1))

    # Materia
    app.materia_btn_create.clicked.connect(lambda: switch_widget(app, 3, 0))
    app.materia_btn_edit.clicked.connect(lambda: switch_widget(app, 3, 0))
    app.materia_btn_search.clicked.connect(lambda: switch_widget(app, 3, 1))
    app.materia_btn_list.clicked.connect(lambda: switch_widget(app, 3, 1))
    app.materia_btn_remove.clicked.connect(lambda: switch_widget(app, 3, 1))

def switch_widget(app, widget_id, index):
    # widget_id:
    #   1: Aluno
    #   2: Curso
    #   3: Materia
    if widget_id == 1:
        if index == 0:
            
        app.aluno_widget.setCurrentIndex(index)
    if widget_id == 2:
        app.curso_widget.setCurrentIndex(index)
    if widget_id == 3:
        app.materia_widget.setCurrentIndex(index)