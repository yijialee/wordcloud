# -*- coding: utf-8  -*-
import cx_Oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

conn = None
isOpen = False
connstr = 'ytdjdt/ytdjdt@sunzdev'
def setConnectStr(str):
    global  connstr, isOpen
    connstr = str
    isOpen = False
def open():
    global conn , isOpen
    if(  isOpen == False):
        conn =_initConn()
def close():
    global conn , isOpen
    if( isOpen ):
        conn.close()
        isOpen = False
        print "关闭数据库连接"
def _initConn():
    global conn ,isOpen ,connstr
    print "打开数据库连接"
    conn = cx_Oracle.connect( connstr )
    isOpen = True
    return conn;


def query(sql):
    global conn , isOpen
    open()
    #conn = initConn()
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()#[0][0].read()
    cursor.close()
    #conn.close()
    #print res
    return res

def execute(sql):
    global conn , isOpen
    open()
    #conn = initConn()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    #conn.close()


if __name__ == "__main__":
    open()
    sql = "select typecode from T_S_TYPE t  where t.typename like '%事业单位%' "
    res = query(sql)
    close()
    #open()
    print res