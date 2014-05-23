__author__ = 'wangss'
#written for DB controller

def test():
    print("")


class Conn(object):
    "connect  base class"

    def __init__(self, name, user, password):
        self.name = name
        self.user = user
        self.password = password


if __name__ == '__main__':
    test()