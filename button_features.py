
from PyQt4.QtGui import QMessageBox
from PyQt4 import QtGui, QtCore

from models import *
import button_listener as bl
from crud import *

def create_aluno(app):
    # pega dados dos campos
    nome = str(app.aluno_input_nome.text())
    idade = str(app.aluno_input_idade.value())
    matricula = str(app.aluno_input_matricula.value())
    semestre = str(app.aluno_input_semestre.value())
    curso = str(app.aluno_input_curso.currentText())
    if nome != '':
        a = Aluno(None, nome, matricula, curso, semestre, idade)
        # AlunoDAO
        AlunoDAO.insert(a)
        # popula a tabela
        row = app.aluno_table.rowCount()
        app.aluno_table.insertRow(row)
        app.aluno_table.setItem(row, 0, QtGui.QTableWidgetItem(nome))
        app.aluno_table.setItem(row, 1, QtGui.QTableWidgetItem(idade))
        app.aluno_table.setItem(row, 2, QtGui.QTableWidgetItem(matricula))
        app.aluno_table.setItem(row, 3, QtGui.QTableWidgetItem(semestre))
        app.aluno_table.setItem(row, 4, QtGui.QTableWidgetItem(curso))
        # apaga dados dos campos
        app.aluno_input_nome.clear()
        app.aluno_input_idade.setValue(0)
        app.aluno_input_matricula.setValue(0)
        app.aluno_input_semestre.setValue(1)
        app.aluno_input_curso.setCurrentIndex(0)
        QMessageBox.information(app, 'Sucesso!', 'Aluno criado com sucesso!')
    else:
        QMessageBox.critical(app, 'Erro!', 'Todos os campos devem ser preenchidos!')

def create_curso(app):
    nome = app.curso_input_nome.text()
    carga_horaria = str(app.curso_input_duracao.value())
    if nome != '':
        c = Curso(None, nome, carga_horaria)
        CursoDAO.add(c)
        row = app.curso_table.rowCount()
        app.curso_table.insertRow(row)
        app.curso_table.setItem(row, 0, QtGui.QTableWidgetItem(nome))
        app.curso_table.setItem(row, 1, QtGui.QTableWidgetItem(carga_horaria))
        try:
            num_alunos = str(CursoDAO.get_numb_alun(CursoDAO.getcurso()))
            app.curso_table.setItem(row, 2, QtGui.QTableWidgetItem(num_alunos))
        except:
            app.curso_table.setItem(row, 2, QtGui.QTableWidgetItem('Desconhecido'))
        QMessageBox.information(app, 'Sucesso!', 'Curso criado com sucesso!')
    else:
        QMessageBox.critical(app, 'Erro!', 'Todos os campos devem ser preenchidos!')

def create_materia(app):
    nome = app.materia_input_nome.text()
    num_aulas = app.materia_input_aulas.value()
    if nome != '':
        m = Materia(None, nome, num_aulas)
        MateriaDAO.add(m)
        row = app.materia_table.rowCount()
        app.materia_table.insertRow(row)
        app.materia_table.setItem(row, 0, QtGui.QTableWidgetItem(nome))
        app.materia_table.setItem(row, 1, QtGui.QTableWidgetItem('Desconhecido'))
        app.materia_table.setItem(row, 2, QtGui.QTableWidgetItem(num_aulas))
        QMessageBox.information(app, 'Sucesso!', 'Materia criada com sucesso!')
    else:
        QMessageBox.critical(app, 'Erro!', 'Todos os campos devem ser preenchidos!')

def nota_aluno(app):
    matricula = int(app.aluno_input_aluno.currentText())
    materia = app.aluno_input_materia.currentText()
    np1 = app.aluno_input_np1.value()
    np2 = app.aluno_input_np2.value()
    np3 = app.aluno_input_np3.value()
    nf = app.aluno_input_np3.value()
    situacao = app.aluno_input_situacao.text()

    n = Nota(None, np1, np2, matricula, materia)
    if situacao == '':
        NotaDAO.add(n)
        # mudar situação
    # + if dependendo da situação
    #setnp1, setnp2, setnp3

def edit_aluno(app):
    # pega a linha selecionada
    selected_item = app.aluno_table.currentRow()
    if selected_item != -1:
        # pega os dados da linha
        nome = str(app.aluno_table.item(selected_item, 0).text())
        idade = int(app.aluno_table.item(selected_item, 1).text())
        matricula = int(app.aluno_table.item(selected_item, 2).text())
        semestre = int(app.aluno_table.item(selected_item, 3).text())
        curso = str(app.aluno_table.item(selected_item, 4).text())
        # coloca nos campos para editar
        app.aluno_input_nome.setText(nome)
        app.aluno_input_idade.setValue(idade)
        app.aluno_input_matricula.setValue(matricula)
        app.aluno_input_semestre.setValue(semestre)
        curso_index = app.aluno_input_curso.findText(curso)
        app.aluno_input_curso.setCurrentIndex(curso_index)
        bl.switch_widget(app, 1, 0)
    else:
        QMessageBox.critical(app, 'Erro!', 'Selecione um aluno para editar!')

def edit_curso(app):
    # pega a linha selecionada
    selected_item = app.curso_table.currentRow()
    if selected_item != -1:
        # pega os dados da linha
        nome = str(app.curso_table.item(selected_item, 0).text())
        carga_horaria = int(app.curso_table.item(selected_item, 1).text())
        # coloca nos campos para editar
        app.curso_input_nome.setText(nome)
        app.curso_input_duracao.setValue(carga_horaria)
        bl.switch_widget(app, 2, 0)
    else:
        QMessageBox.critical(app, 'Erro!', 'Selecione um aluno para editar!')

def edit_materia(app):
    # pega a linha selecionada
    selected_item = app.materia_table.currentRow()
    if selected_item != -1:
        # pega os dados da linha
        nome = str(app.materia_table.item(selected_item, 0).text())
        num_aulas = int(app.materia_table.item(selected_item, 1).text())
        # coloca nos campos para editar
        app.matricula_input_nome.setText(nome)
        app.matricula_input_aulas.setValue(num_aulas)
        bl.switch_widget(app, 3, 0)
    else:
        QMessageBox.critical(app, 'Erro!', 'Selecione um aluno para editar!')

def remove_aluno(app):
    # pega a linha selecionada
    selected_item = app.aluno_table.currentRow()
    if selected_item != -1:
        # pega os dados da linha
        matricula = int(app.aluno_table.item(selected_item, 2).text())
        resp = QMessageBox.question(app, 
        'Confirmação', 'Realmente deseja deletar o aluno de matricula {0}?'.format(matricula),
        QMessageBox.Ok | QMessageBox.Cancel)
        if resp == QMessageBox.Ok:
            # AlunoDAO delete
            app.aluno_table.removeRow(selected_item)
    else:
        QMessageBox.critical(app, 'Erro!', 'Selecione um aluno para deletar!')

def remove_curso(app):
    # pega linha selecionada
    selected_item = app.curso_table.currentRow()
    if selected_item != -1:
        # pega os dados da linha
        nome = str(app.curso_table.item(selected_item, 0).text())
        resp = QMessageBox.question(app, 
        'Confirmação', 'Realmente deseja deletar o curso {0}?'.format(nome),
        QMessageBox.Ok | QMessageBox.Cancel)
        if resp == QMessageBox.Ok:
            # CursoDAO delete
            app.curso_table.removeRow(selected_item)

def remove_materia(app):
    # pega linha selecionada
    selected_item = app.materia_table.currentRow()
    if selected_item != -1:
        # pega os dados da linha
        nome = str(app.materia_table.item(selected_item, 0).text())
        resp = QMessageBox.question(app, 
        'Confirmação', 'Realmente deseja deletar a materia {0}?'.format(nome),
        QMessageBox.Ok | QMessageBox.Cancel)
        if resp == QMessageBox.Ok:
            # CursoDAO delete
            app.materia_table.removeRow(selected_item)