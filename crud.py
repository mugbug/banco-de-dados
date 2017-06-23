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

class CursoDAO(object):

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




