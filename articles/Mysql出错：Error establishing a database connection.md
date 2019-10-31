Error establishing a database connection

### 1、查看mysql运行状态
~~~
$ systemctl status mysqld 
~~~

### 2、重启mysql
~~~
systemctl restart mysqld
~~~

### 3、查看mysql日志
~~~
vi /var/log/mysqld.log

2017-11-30T21:56:40.544057Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
~~~

### 4、查看运行服务
~~~
netstat -plt

output：
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 localhost:cslistener    0.0.0.0:*               LISTEN      16030/php-fpm: pool
tcp        0      0 0.0.0.0:http            0.0.0.0:*               LISTEN      23057/nginx: master
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN      871/sshd
tcp        0      0 localhost:smtp          0.0.0.0:*               LISTEN      1055/master
tcp        0      0 0.0.0.0:sunwebadmins    0.0.0.0:*               LISTEN      980/python
tcp6       0      0 [::]:mysql              [::]:*                  LISTEN      21052/mysqld
tcp6       0      0 [::]:http               [::]:*                  LISTEN      23057/nginx: master
tcp6       0      0 [::]:ftp                [::]:*                  LISTEN      15034/vsftpd
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      871/sshd
tcp6       0      0 localhost:smtp          [::]:*                  LISTEN      1055/master

The netstat command prints information about our server's networking system. In this case, we want the names of programs (-p) listening for connections (-l) on a tcp socket (-t).
~~~

### 5、搜索日志文件
~~~
zgrep -a "allocate memory" /var/log/mysqld.log 

output:
2017-11-30T13:06:20.028071Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
2017-11-30T13:06:35.421554Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
2017-11-30T13:06:35.859330Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
2017-11-30T13:11:50.792712Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
2017-11-30T13:11:51.415883Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
2017-11-30T13:11:51.911339Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
2017-11-30T13:11:52.460354Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
2017-11-30T13:11:52.914341Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
2017-11-30T21:52:05.059221Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
2017-11-30T21:52:05.568186Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
2017-11-30T21:52:06.085132Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
2017-11-30T21:52:06.545330Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
2017-11-30T21:56:38.707143Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
2017-11-30T21:56:39.046362Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
2017-11-30T21:56:39.546123Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
2017-11-30T21:56:40.074679Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool
2017-11-30T21:56:40.544057Z 0 [ERROR] InnoDB: Cannot allocate memory for the buffer pool

zgrep will search through log files.
~~~

### 6、查看内存使用情况
~~~
1)  cat /proc/meminfo

查看RAM使用情况最简单的方法是通过/proc/meminfo。
这个动态更新的虚拟文件实际上是许多其他内存相关工具(如：free / ps / top)等的组合显示。
/proc/meminfo列出了所有你想了解的内存的使用情况。
进程的内存使用信息也可以通过/proc/<pid>/statm 和 /proc/<pid>/status 来查看。

2)   free -m(t)
output:
              total        used        free      shared  buff/cache   available
Mem:            990         622         118          49         250         170
Swap:             0           0           0
Total:          990         648         102

free命令是一个快速查看内存使用情况的方法，它是对 /proc/meminfo 收集到的信息的一个概述。

3) top

4)  vmstat -s
vmstat命令显示实时的和平均的统计，覆盖CPU、内存、I/O等内容。例如内存情况，不仅显示物理内存，也统计虚拟内存。

5)  ps aux --sort -rss

~~~

### 7、更改mysql配置，重启mysql
~~~
vi /etc/my.cnf

innodb_buffer_pool_size = 128M
key_buffer_size = 120M
max_connections = 500 #增加mysql连接数
wait_timeout = 10 #断开超过10秒的连接

systemctl restart mysqld
~~~


https://www.digitalocean.com/community/tutorials/how-to-debug-the-wordpress-error-establishing-database-connection

http://www.wpbeginner.com/wp-tutorials/how-to-fix-the-error-establishing-a-database-connection-in-wordpress/
