# coding: UTF-8
import MySQLdb
from connector import DataBaseConnector


def connect():
    conn = DataBaseConnector()
    conn.get_db()
    if conn != 1:
        return conn
    return conn

class AlunoDAO(object):

    @staticmethod
    def insert(aluno):
        db = connect()

        if db != 1:
            cur = db.cursor()
            try:
                cur.execute("INSERT INTO aluno (Nome, Matricula, Curso, SemestreAtual, Idade, Curso_idCurso)"
                            "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')"
                            .format(aluno.nome, aluno.matricula, aluno.curso, aluno.semestre, aluno.idade, aluno.curso))
                db.commit()
            except MySQLdb.Error:
                print "Error to execute script"
            finally:
                print "Concluido"
                cur.close()




