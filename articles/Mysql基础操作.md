### 登录数据库
~~~
mysql -u root -p
~~~

### 查询数据库
~~~
show databases;
~~~

### 创建数据库
~~~
create database test;
~~~

### 切换数据库
~~~
use test;
~~~

### 查看当前数据库；
~~~
select database();
~~~

### 查询表
~~~
show tables;
~~~

### 创建表
~~~
CREATE TABLE `house`.`zz` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(256) NULL,
  `url` VARCHAR(256) NULL,
  `info` VARCHAR(256) NULL,
  `position` VARCHAR(256) NULL,
  `follow` VARCHAR(256) NULL,
  `total_price` VARCHAR(256) NULL,
  `unit_price` VARCHAR(256) NULL,
  `tags` VARCHAR(256) NULL,
  PRIMARY KEY (`id`)
);

create tabel user
(
    id int unsigned not null auto_increment primary key,
    name char(10) not null,
    age tinyint unsigned not null,
    birth datetime
);
~~~

### 修改表
~~~
ALTER TABLE `house`.`zz_f` 
CHANGE COLUMN `title` `title` VARCHAR(256) NOT NULL ;
~~~

### 清空表
~~~
truncate table house.zz
~~~

### in查询
~~~
SELECT * FROM house.zz where id in( 740, 1118, 1644, 2779, 2947)
~~~

### 插入数据
~~~
INSERT INTO `house`.`zz_f`( `title` ) VALUES ('hello') 
~~~

### 删除数据
~~~
DELETE FROM `house`.`zz_f` WHERE (`id` = '45');
~~~

### 更新数据
~~~
UPDATE `house`.`zz_f` SET `floor` = '33' WHERE (`id` = '45');
~~~

### 排序
~~~
// 升序
SELECT * FROM house.zz_f order by total_price asc

// 降序
SELECT * FROM house.zz_f order by total_price desc

// 条件查询并降序
SELECT * FROM house.zz_f where total_price < 100 order by focus desc 

// 多个字段排序
SELECT * FROM house.zz_f where total_price < 100 order by total_price desc,focus desc 
~~~

### NULL查询
~~~
SELECT * FROM house.zz_f where floor IS NULL
~~~

### count(*)查询
~~~
SELECT COUNT(*) FROM house.zz_f where floor IS NULL
~~~

### 复制表
~~~
// 1. 复制表结构及数据到新表
create table tb_new select * from tb;

// 2. 复制表结构到新表
create tabel tb_new like tb
or
create table tb_new select * from tb limit 0
or
create table tb_new select * from tb where <>

// 3. 复制旧表数据到新表
a.表结构一样
insert into tb_new select * from tb

b. 表结构不一样
insert into tb_new (field1,field2,...) select field1,field2,... from tb
~~~

### 参考
mysql order by
https://www.cnblogs.com/stsinghua/p/6418363.html

mysql copy table
https://www.cnblogs.com/Weirdo-world/p/9370690.html
