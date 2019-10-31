## 使用–skip-grant-tables重置MySQL Root密码  

1、停止MySQL服务
~~~
$ systemctl stop mysqld.service     # for distros using systemd 
$ /etc/init.d/mysqld stop           # for distros using init
~~~

2、使用–skip-grant-tables启动服务 
~~~
$ mysqld --skip-grant-tables --user=mysql &
~~~

3、连接MySQL
~~~
$ mysql
~~~

4、重新加载授权
~~~
$ FLUSH PRIVILEGES;
~~~

5、修改密码
~~~
$ ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_passowrd';

or

$ UPDATE mysql.user SET authentication_string = PASSWORD('386mysql.')
WHERE User = 'root' AND Host = 'localhost';
~~~

6、停止MySQL服务并以正常模式启动
~~~
# systemctl stop mysqld.service        # for distros using systemd 
# systemctl restart mysqld.service     # for distros using systemd 

# /etc/init.d/mysqld stop              # for distros using init
# /etc/init.d/mysqld restart           # for distros using init
~~~

7、使用新密码连接MySQL  
~~~
$ mysql -u root -p
~~~

参考：
https://www.tecmint.com/reset-root-password-in-mysql-8/

http://www.cnblogs.com/doctorJoe/p/5337510.html
