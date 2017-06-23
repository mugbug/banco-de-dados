# coding: UTF-8
import MySQLdb

class DataBaseConnector(object):

    @staticmethod
    def get_db():
        db_connection = False
        try:
            db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='mydb')
        except MySQLdb.Error as err:
            e = "Database connection error [%d]: %s" % (err.args[0], err.args[1])
        else:
            db_connection = True
        finally:
            if db_connection:
                print 'Database connection successful!'
                return db
            else:
                print e
                return 1