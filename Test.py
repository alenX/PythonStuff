__author__ = 'wangss'
#written for DB controller
from ConMysql import *


def test():
    sqlconn = ConMysql("localhost", "root", "1128", "test", "utf8")
    sqlconn.deletesql("DELETE FROM STUDENT WHERE ID=1")


class Conn(object):
    "connect  base class"

    def __init__(self, name, user, password):
        self.name = name
        self.user = user
        self.password = password


if __name__ == '__main__':
    test()