#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mysql.connector
# 打开数据库连接
conn = mysql.connector.connect(user='root', password='123456', database='hdu')
cursor = conn.cursor()
# 使用execute方法执行SQL语句
cursor.execute('insert into word values (%s,%s,%s)',['english','chinese',10])
# 使用 fetchone() 方法获取一条数据
conn.commit()
# 关闭数据库连接
conn.close()
