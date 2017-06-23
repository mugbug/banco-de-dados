from connector import DataBaseConnector
import crud
import models

if __name__ == '__main__':
    '''
    curso = models.Curso(None, 'Eng Automacao', 800)
    crud.CursoDAO().add(curso)
    '''
    '''
    c = crud.CursoDAO()
    cursos = c.getcurso()
    for curso in cursos:
        num = c.get_numb_alun(curso[0])
        print curso
        print num
    '''

    #print crud.AlunoDAO().getmaterias(2)


    print crud.NotaDAO().getalunonota(2,2)

