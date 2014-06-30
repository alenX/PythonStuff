# -*- encoding: utf-8 -*-
__author__ = 'wangss'
# 数据处理脚本
import xlrd


def sqlExcute():
    file1 = open("E://111.sql")
    file2 = open("E://222.sql")
    re = []
    for i in file2:
        # print i.decode('gbk')
        if i.find("values") > -1:
            re.append(i.split("values")[1].split(",")[0][3:-1])
    for j in file1:
        if j.find("values") > -1:
            temp = j.split("values")[1].split(",")[0][3:-1]
            if temp not in re:
                print 'insert into wf_process_type (TYPE_ID, TYPE_NAME, DESCRIPTION, DISPLAY_ORDER) ' + j.decode('gbk')


def excelExc(path):
    re = []
    ex = xlrd.open_workbook(path)
    table = ex.sheets()[0]
    rownum = table.nrows
    for i in range(rownum):
        row = table.row_values(i)
        # print row[2]
        if row[2] not in re:
            re.append(row[2])
    print len(re)
    return re


if __name__ == '__main__':
    re1 = excelExc("E://222.xls")
    re2 = excelExc("E://111.xls")

    temp = []
    for i in re1:
        if i not in re2:
            temp.append(i)

    print len(temp)
    f = open("E://222.sql")
    m = 0
    for j in f:
        if j.find("values") > -1:
            tt = j.split('(')[1].split(',')[1][2:-1]
            # print tt.decode('gbk')
            if tt.decode('gbk') in temp:
                m += 1
                print 'insert into wf_bzns_conf (PROC_DEF_UNIQUE_ID, NAME, REFUSE_ACT_FLAG, BZNS_TABLE, BZNS_STATE_FIELD, BZNS_STATE_VALUE, BZNS_WHERE, MSG_TYPE, BY, LOG_BZNS_CODE, BZNS_PROCESS_ID, BZNS_INDV_CUST_CODE_FIELD, BZNS_MONEY_FIELD, BZNS_CURCD_FIELD, IN_USE)  ' + j.decode(
                    'gbk')
                # print

