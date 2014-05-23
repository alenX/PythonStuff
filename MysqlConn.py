__author__ = 'wangss'
import MySQLdb  #the support for mysql


def conn():
    try:
        conn = MySQLdb.connect(host="localhost", user="root", passwd="1128", db="test", charset="utf8")
        cursor = conn.cursor()
        count = cursor.execute("SELECT * FROM STUDENT")

        result = cursor.fetchmany(count)
        for i in result:
            for a in i:
                print(a)  #the charset
        cursor.close()
        conn.close()
    except MySQLdb.Error, e:
        print("%d,%s" % (e.args[0], e.args[1]))


if __name__ == '__main__':
    conn()

