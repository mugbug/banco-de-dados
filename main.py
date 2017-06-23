from connector import DataBaseConnector
import crud

if __name__ == '__main__':
    c = crud.CursoDAO()
    cursos = c.getcurso()
    for curso in cursos:
        num = c.get_numb_alun(curso[0])
        print curso
        print num


