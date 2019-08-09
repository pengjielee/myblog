### 导入pymysql
~~~
import pymysql.cursors
~~~

### 连接数据库
~~~
def connect():
  return pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='386mysql.',
                         database='test',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
~~~

### 插入数据
~~~
def insert():
	conn = connect()
	cursor = conn.cursor()
	try:
		sql = "INSERT INTO `users` (`email`) VALUES (%s)"
		cursor.execute(sql, ('386276251@qq.com'))
		conn.commit()
	except Exception as e:
		print(e)
		conn.rollback()
	finally:
		cursor.close()
		conn.close()
~~~

### 插入多条数据
~~~
def insertMany():
	conn = connect()
	cursor = conn.cursor()
	try:
		emails = [ '386276252@qq.com', '386276253@qq.com', '386276254@qq.com']
		sql = "INSERT INTO `users` (`email`) VALUES (%s)"
		cursor.executemany(sql, emails)
		conn.commit()
	except Exception as e:
		print(e)
		conn.rollback()
	finally:
		cursor.close()
		conn.close()
~~~

### 删除数据
~~~
def delete():
	conn = connect()
	cursor = conn.cursor()
	try:
		sql = "DELETE FROM `users` WHERE `id`=%s "
		cursor.execute(sql, (12))
		conn.commit()
	except Exception as e:
		print(e)
		conn.rollback()
	finally:
		cursor.close()
		conn.close()
~~~

### 更新数据
~~~
def update():
	conn = connect()
	cursor = conn.cursor()
	try:
		sql = "UPDATE `users` SET `email`=%s WHERE `id`=%s "
		cursor.execute(sql, ('hello@google.com',12))
		conn.commit()
	except Exception as e:
		print(e)
		conn.rollback()
	finally:
		cursor.close()
		conn.close()
~~~

### 查询数据
~~~
def query():
	conn = connect()
	cursor = conn.cursor()

	sql = "SELECT `id`, `email` FROM `users` limit 5"
	cursor.execute(sql)

	results = cursor.fetchall()
	for row in results:
		print(row)

	cursor.close()
	conn.close()
~~~
