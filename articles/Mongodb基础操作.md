1、查看数据库
~~~
show dbs;
~~~

2、切换库
~~~
use wangyi;
~~~

3、查看表
~~~
show tables;
~~~

4、查询集合
~~~
db.playlist.find({})
~~~

5、格式化集合
~~~
db.playlist.find({}).pretty()
~~~

6、条件查询
~~~
$ db.playlist.find({ '_id': { '$gt' :ObjectId('5cdbc648421aa93fc037e668')} }) 
~~~

7、获取时间信息
~~~
$ ObjectId('5cdbc648421aa93fc037e668').getTimestamp()
~~~

8、去除重复数据
~~~
$ db.songs.distinct('song_id')
~~~

9、获取重复数据
~~~
$ db.songs.aggregate([
    { $group: { _id : '$song_id', count: { $sum : 1 } } },
    { $match: { count: { '$gt' : 1} } }
])
~~~

10、清屏
~~~
$ cls

or

$ Ctrl + l
~~~

11、删除集合
~~~
db.songs.drop()
~~~

12、for循环增加索引
~~~
for index, item in enumerate([3,4,5]):
~~~

13、复制集合
~~~
db.collection_source.find({}).forEach(function(item){
    db.collection_target.insert_one(item);
})
~~~


https://docs.mongodb.com/manual/reference/command/aggregate/index.html
