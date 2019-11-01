### 1. 创建mongodb数据库备份目录
~~~
> mkdir -p /data/mongodb_bak/mongodb_bak_now
> mkdir -p /data/mongodb_bak/mongodb_bak_list
~~~

### 2. 创建mongodb数据库备份脚本
~~~
> vi /home/backup_mongodb.sh

#!/bin/bash
#backup MongoDB

#mongodump命令路径
DUMP=/usr/bin/mongodump
#临时备份目录
OUT_DIR=/data/mongodb_bak/mongodb_bak_now

#备份存放路径
TAR_DIR=/data/mongodb_bak/mongodb_bak_list
#获取当前系统时间
DATE=`date +%Y_%m_%d`
#数据库账号
DB_USER=root
#数据库密码
DB_PASS=123
#DAYS=15代表删除15天前的备份，即只保留近15天的备份
DAYS=15
#最终保存的数据库备份文件
TAR_BAK="mongodb_bak_$DATE.tar.gz"

cd $OUT_DIR
rm -rf $OUT_DIR/*
mkdir -p $OUT_DIR/$DATE
#备份全部数据库
$DUMP -h 127.0.0.1:27017 -d "personal" -o $OUT_DIR/$DATE
#压缩为.tar.gz格式
tar -zcvf $TAR_DIR/$TAR_BAK $OUT_DIR/$DATE
#删除15天前的备份文件
find $TAR_DIR/ -mtime +$DAYS -delete

exit
~~~

### 3. 修改文件属性，使其可执行
~~~
> chmod +x /home/crontab/mongod_bak.sh
~~~

### 4. 修改/etc/crontab, 添加计划任务
~~~
> vi /etc/crontab

SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed
0 0 * * * root /home/backup_mongodb.sh # 每天24:00执行备份
~~~

### 5. 重新启动crond使设置生效
~~~
> /bin/systemctl reload crond.service  #重新载入配置

> systemctl status crond

> systemctl enable crond.service #开机自动启动
~~~

mongodb 定时备份
https://www.cnblogs.com/zhang-ke/p/7804503.html
https://www.linuxidc.com/Linux/2016-11/137560.htm