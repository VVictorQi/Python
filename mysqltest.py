import pymysql
conn = pymysql.connect(user='root', passwd='', host='localhost', port=3306, db='test')
cursor=conn.cursor()
cursor.execute('create table user1(id varchar(20)primary key,name varchar(20))')
cursor.execute('insert into user1 (id,name) values (%s,%s)',['001','VIctorqi'])
cursor.rowcount
conn.commit()
cursor.close()

cursor=conn.cursor()
cursor.execute('select * from user where id=%s',['001'])
values=cursor.fetchall()
print (values)
cursor.close()
conn.close()