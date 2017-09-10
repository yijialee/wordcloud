#coding=utf-8
__author__ = 'licha'

import MySQLdb



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

#cur = conn.cursor()
def _initConn():
    global conn , isOpen
    print "打开数据库连接"
    conn =  MySQLdb.connect(
        host='114.215.201.111',
        port = 3306,
        user='hdm1310272',
        passwd='lc100200',
        db ='hdm1310272_db',
        charset = 'utf8'
        )
    isOpen = True
    return conn;
#charset = 'utf8'

def query(sql):
    global conn , isOpen
    open()
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()#[0][0].read()
    cursor.close()
    #print res
    return res

def execute(_sql):
    global conn , isOpen
    open()
    sql = _sql #_sql.decode('utf8').encode('gbk')
    #print sql
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
#创建数据表
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")


#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")



if __name__ == "__main__":
    open()
    sql = "SELECT * FROM `sys_user` LIMIT 0, 1000"
    res = query(sql)
    print res
    #sql="insert into zhilian (name ,salary,location,time,company) values('JAVA','8001-10000','北京','今天','北京') "
    #execute(sql)
    close()