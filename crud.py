# coding: UTF-8
import MySQLdb
from connector import DataBaseConnector


def connect():
    conn = DataBaseConnector()
    db = conn.get_db()
    if conn != 1:
        return db
    return db

class AlunoDAO(object):

    @staticmethod
    def insert(aluno):
        db = connect()
        print db

        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("INSERT INTO aluno (Nome, Matricula, SemestreAtual, Idade, Curso_idCurso)"
                            "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')"
                            .format(aluno.nome, aluno.matricula, aluno.semestre, aluno.idade, aluno.curso))
                db.commit()
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                cur.close()

    @staticmethod
    def getaluno():
        db = connect()

        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("select * from aluno")
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                ans = cur.fetchall()
                cur.close()
                return ans

    @staticmethod
    def getidaluno(mat):
        db = connect()

        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("select idAluno from aluno where Matricula like '{0}'"
                            .format(mat))
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                ans = cur.fetchall()
                cur.close()
                return ans

    @staticmethod
    def getmaterias(id):
        db = connect()

        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("select materia.Nome from materia where materia.idMateria in" +
                            "(select Materia_idMateria from aluno_has_materia where Aluno_idAluno = '{0}')"
                            .format(id))
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                ans = cur.fetchall()
                cur.close()
                return ans

class CursoDAO(object):

    @staticmethod
    def add(curso):
        db = connect()

        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("insert into curso (Nome, HorasDuracao) values ('{0}', '{1}')"
                            .format(curso.nome, curso.horasduracao))
                db.commit()
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                cur.close()

    @staticmethod
    def remove(id):
        db = connect()

        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("delete from curso where idCurso = '{0}'"
                            .format(id))
                db.commit()
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                cur.close()

    @staticmethod
    def getcurso():
        db = connect()

        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("select * from curso")
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                ans = cur.fetchall()
                cur.close()
                return ans

    @staticmethod
    def get_numb_alun(cursoid):
        db = connect()

        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("select count(*) from aluno where Curso_idCurso = '{0}';"
                            .format(cursoid))
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                ans = cur.fetchall()
                cur.close()
                return ans


class MateriaDAO(object):

    @staticmethod
    def add(materia):
        db = connect()

        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("insert into materia (Nome,NumAulas) values ('{0}', '{1}')"
                            .format(materia.nome, materia.numaulas))
                db.commit()
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                cur.close()

    @staticmethod
    def remove(id):
        db = connect()

        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("delete from materia where idCurso = '{0}'"
                            .format(id))
                db.commit()
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                cur.close()

    @staticmethod
    def getmaterias():
        db = connect()

        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("select materia.Nome, curso.Nome, materia.NumAulas from materia " +
                            "inner join curso_has_materia on Materia_idMateria = idMateria " +
                            "inner join curso on Curso_idCurso = curso.idCurso;")
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                ans = cur.fetchall()
                cur.close()
                return ans

    @staticmethod
    def getidmateria(materia):
        db = connect()

        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("select idMateria from materia where Nome like '{0}'"
                            .format(materia))
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                ans = cur.fetchall()
                cur.close()
                return ans

class NotaDAO():

    @staticmethod
    def add(nota):
        db = connect()

        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("insert into nota (NP1,NP2,Aluno_idAluno,Materia_idMateria)" +
                            "values ('{0}', '{1}', '{2}', '{3}')"
                            .format(nota.NP1, nota.NP2, nota.alunoid, nota.materiaid))
                db.commit()
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                cur.close()

    @staticmethod
    def getalunonota(idAluno, idMateria):
        db = connect()

        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("select * from nota where Aluno_idAluno = '{0}' and Materia_idMateria = '{1}'"
                            .format(idAluno, idMateria))
                db.commit()
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                ans = cur.fetchall()
                cur.close()
                return ans

    @staticmethod
    def setnp1(np1, matricula, materia):

        idAluno = AlunoDAO.getidaluno(matricula)[0][0]
        idMateria = MateriaDAO.getidmateria(materia)[0][0]

        db = connect()
        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("insert into nota (NP1, Aluno_idAluno, Materia_idMateria) values ('{0}', '{1}', '{2}')"
                            .format(np1, idAluno, idMateria))
                db.commit()
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                cur.close()

    @staticmethod
    def setnp2(np2, matricula, materia):

        idAluno = AlunoDAO.getidaluno(matricula)[0][0]
        idMateria = MateriaDAO.getidmateria(materia)[0][0]

        db = connect()
        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("update nota set NP2 = '{0}' where Aluno_idAluno = '{1}' and Materia_idMateria = '{2}'"
                            .format(np2, idAluno, idMateria))
                db.commit()
            except MySQLdb.Error as e:
                print e
            finally:
                cur.close()

    @staticmethod
    def setnp3(np3, matricula, materia):

        idAluno = AlunoDAO.getidaluno(matricula)[0][0]
        idMateria = MateriaDAO.getidmateria(materia)[0][0]

        db = connect()
        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("update nota set NP3 = '{0}' where Aluno_idAluno = '{1}' and Materia_idMateria = '{2}'"
                            .format(np3, idAluno, idMateria))
                db.commit()
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                cur.close()