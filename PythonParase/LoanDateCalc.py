# -*- encoding=utf-8-*-
__author__ = 'wangss'


def isleapyear(year):  # 是否为闰年
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def getactdateby(date, term):
    year = date[0]
    month = date[1]
    day = date[3]


