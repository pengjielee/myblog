CSV (Comma Separated Values)，逗号分隔值，有时也称为字符分隔值，因为分隔字符也可以不是逗号。

### 引入python csv
~~~
import csv
~~~

### 使用csv reader读取
~~~
# contacts.csv
10,jim,18614023231
11,tom,18614023232
12,mike,18614023233

with open(contacts.csv,newline='') as csvfile:
	reader=csv.reader(csvfile,delimiter=',')
	for row in reader:
		print(row)
		#print(', '.join(row))
		#print(row[0]+','+row[1]+','+row[2])

output:
['10', 'jim', '18614023231']
['11', 'tom', '18614023232']
['12', 'mike', '18614023233']
~~~

### 使用csv reader读取其他分隔符
~~~
# contacts.csv
10|jim|18614023231
11|tom|18614023232
12|mike|18614023233

with open(contacts.csv,newline='') as csvfile:
	reader=csv.reader(csvfile,delimiter='|')
	for row in reader:
		print(row)

output:
['10', 'jim', '18614023231']
['11', 'tom', '18614023232']
['12', 'mike', '18614023233']
~~~

### 使用csv dictreader读取
~~~
# contacts.csv
id,name,phone
10,jim,18614023231
11,tom,18614023232
12,mike,18614023233

with open(contacts.csv, newline='') as csvfile:
	reader=csv.DictReader(csvfile,delimiter=',')
	for row in reader:
		print(row)
		#print(row['id'], row['name'],row['phone'])

output:
OrderedDict([('id', '10'), ('name', 'jim'), ('phone', '18614023231')])
OrderedDict([('id', '11'), ('name', 'tom'), ('phone', '18614023232')])
OrderedDict([('id', '12'), ('name', 'mike'), ('phone', '18614023233')])
~~~

### 使用csv dictreader自定义filednames读取
~~~
# contacts.csv
10,jim,18614023231
11,tom,18614023232
12,mike,18614023233

with open(contacts.csv, newline='') as csvfile:
	fieldnames=[ 'id', 'name', 'phone' ]
	reader=csv.DictReader(csvfile,fieldnames=fieldnames)
	for row in reader:
		print(row)
		#print(row['id'], row['name'],row['phone'])

output:
OrderedDict([('id', '10'), ('name', 'jim'), ('phone', '18614023231')])
OrderedDict([('id', '11'), ('name', 'tom'), ('phone', '18614023232')])
OrderedDict([('id', '12'), ('name', 'mike'), ('phone', '18614023233')])
~~~

### 使用csv writer写入
~~~
# contacts.csv
-- empty

with open(contacts.csv, 'w', newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=',',
	quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['20', 'peng', '18614023235'])
		writer.writerow(['21', 'jie', '18614023236'])

result:
# contacts.csv
20,peng,18614023235
21,jie,18614023236
~~~

### 使用csv dicrwriter写入
~~~
# contacts.csv
-- empty

with open(contacts.csv, 'w', newline='') as csvfile:
	fieldnames=['id', 'name', 'phone']
	writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerow({'id': '22', 'name': 'jie', 'phone': '18614023235'})

result:
# contacts.csv
id,name,phone
22,jie,18614023235
~~~

[Python CSV文件读取和写入](https://docs.python.org/3/library/csv.html#csv.QUOTE_MINIMAL)
[Python CSV tutorial](http://zetcode.com/python/csv/)