1、查看python版本/更新pip
~~~
$ python3 --version
$ pip install --upgrade pip
~~~

2、安装
~~~
pip install pymongo
~~~

3、连接mongodb
~~~
from pymongo import MongoClient

# 格式化输出
from pprint import pprint

client = MongoClient('mongodb://localhost:27017/')

# 指定数据库
db = client.wangyi 

# 指定集合
collection = db.playlist
~~~

4、插入
~~~
# 插入单条
result = collection.insert_one({'title':'test'})
pprint(result)

# 插入多条
result = collection.insert_many([{'title':'test1'},{'title':'test2'}])
pprint(result)
~~~

5、查询
~~~
# 查询一条
result = collection.find_one({})
pprint(result)

# 查询多条
results = collection.find({})
pprint(results)
for item in results:
	print(item)

# 条件查询
results = collection.find({'age': {'$lt': 20}})        #小于20
results = collection.find({'age': {'$gt': 20}})        #大于20
results = collection.find({'age': {'$lte': 20}})       #小于等于20
results = collection.find({'age': {'$gte': 20}})       #大于等于20
results = collection.find({'age': {'$ne': 20}})        #不等于20
results = collection.find({'age': {'$in': [20,23]}})   #在[20,23]之间
results = collection.find({'age': {'$nin': [20,23]}})  #不在[20,23]之间

results = collection.find({'name': {'$regex': '^M.*'}}) #名字以M开头
results = collection.find({'name': {'$exists': True}})  #name属性存在
results = collection.find({'age': {'$type': 'int'}}})   #age的类型为int
results = collection.find({'age': {'$mod': [5, 0]}})    #age模5余0 
results = collection.find({'$text': {'$search': 'Mike'}})#text类型的属性中包含Mike字符串
results = collection.find({'$where': 'obj.fans_count == obj.follows_count'})#自身粉丝数等于关注数
~~~

6、count()
~~~
count = collection.find().count()
print(count)
~~~


7、排序
~~~
# 升序
results = collection.find().sort('name', pymongo.ASCENDING)

# 降序
results = collection.find().sort('name', pymongo.DESCENDING)
~~~

9、分页
~~~
results = collection.find().skip(10).limit(10)
~~~

10、更新
~~~
# 更新一条
condition = {'title': 'test'}
item = collection.find_one(condition)
item['title'] = 'test1'
result = collection.update_one(condition, {'$set': item})

# 更新多条
condition = {'title': 'test'}
item = collection.find_one(condition)
item['title'] = 'test1'
result = collection.update_many(condition, {'$set': item})
~~~

11、移除
~~~
result = collection.remove({})
print(result)
~~~

参考： 
Python操作MongoDB看这一篇就够了
https://cloud.tencent.com/developer/article/1151814  

getting started with python and mongodb
https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb  