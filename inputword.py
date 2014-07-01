# -*- encoding=utf-8-*-
__author__ = 'wangss'
#对于小狼毫词库和华宇词库的转换
def ciku(source, result):
    word = open(source)
    rs = open(result, 'w')
    for i in word:
        tt = i.split()
        pinyin = ''
        for j in range(1, len(tt) - 1):
            pinyin += tt[j] + "'"
        txt = tt[0] + " " + pinyin[:-1] + " " + tt[-1] + "\n"
        rs.writelines(txt)


if __name__ == '__main__':
    ciku('a', 'b')