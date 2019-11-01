查看系统信息
~~~
$ uname -a
~~~

查看操作系统版本号
~~~
$ cat /etc/redhat-release
~~~

查看CPU信息
~~~
$ cat /proc/cpuinfo
~~~

查看系统环境变量
~~~
$ env
~~~

查看系统内存及交换分区使用情况
~~~
$ free -m
~~~

查看分区使用情况
~~~
$ df -h
~~~

查看系统运行时间，用户数，负载情况。
~~~
$ uptime
~~~

查看网络配置
~~~
$ ifconfig
or
$ ip addr (centos7)
~~~

查看网络监听和连接状态
~~~
$ netstat
or
$ ss (centos7)
~~~

查看系统进程
~~~
$ ps
~~~

查看系统实时进程状态
~~~
$ top
~~~

查看活动用户
~~~
$ w
~~~

查看用户登录日志
~~~
$ last
~~~

查看用户计划任务
~~~
$ crontab -l
~~~

查看系统服务状态
~~~
$ chkconfig --list
or
$ systemctl list-unit-files
~~~

查看已安装的软件包
~~~
$ rpm -qa
~~~


CentOS怎样查看系统信息
https://jingyan.baidu.com/article/b0b63dbf377e294a48307084.html