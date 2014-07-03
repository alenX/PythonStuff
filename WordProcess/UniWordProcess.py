# -*- encoding=utf-8-*-
__author__ = 'wangss'

f = open("E://luna_pinyin_export.txt", 'r')
r = open("E://result.txt", 'a')
for i in f:
    rs = i.split()
    if len(rs) > 3 and rs[-1] != '1':

        temp = ''
        for j in range(1, len(rs) - 1):
            temp += rs[j] + "'"
        print(rs[0] + ' ' + temp[:-1] + ' ' + '0')
        # r.writelines(rs[0] + ' ' + temp[:-1] + ' ' + '0\n')