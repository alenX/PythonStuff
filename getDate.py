# -*- encoding=utf-8-*-
__author__ = 'wangss'


def isleapyear(year):  # 是否为闰年
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def getactdateby(date, term):
    year = date[0]
    month = date[1]
    day = date[2]

    newday = day

    temp = year * 12 + month - term

    newyear = temp / 12
    newmonth = temp % 12

    if newmonth == 0:
        newmonth = 12
    elif newmonth == 2:
        if isleapyear(newyear):
            if day > 29:
                newday = 29
        else:
            if day > 28:
                newday = 28
    # 1,3,5,7,8,10,12
    elif newmonth in (4, 6, 9, 11):
        if day > 30:
            newday = 30
    return (newyear, newmonth, newday)


if __name__ == '__main__':
    for i in range(1000):
        print getactdateby((2014, 3, 31), i)