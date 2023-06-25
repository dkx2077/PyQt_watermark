import sqlite3

conn = sqlite3.connect("user.db")  # 在此文件所在的文件夹打开或创建数据库文件

c = conn.cursor()  # 设置游标

# 创建一个含有id，name，password字段的表
c.execute('''CREATE TABLE user
      (id INTEGER PRIMARY KEY AUTOINCREMENT ,
       name TEXT NOT NULL ,
       password TEXT NOT NULL )''')

conn.commit()  # python连接数据库默认开启事务，所以需先提交
conn.close()  # 关闭连接