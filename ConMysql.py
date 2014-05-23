__author__ = 'wangss'

import MySQLdb


class ConMysql(object):  #the class of conn
    def __init__(self, host, user, passwd, db, charset):
        conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, charset=charset)
        self.cursor = conn.cursor()
        self.conn = conn

    def deletesql(self, sqlstr):
        self.cursor.execute(sqlstr)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()