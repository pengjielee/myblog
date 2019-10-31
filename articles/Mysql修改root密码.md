~~~
> sudo mysqld_safe --skip-grant-tables

mysqld --skip-grant-tables

> mysql

> ALTER USER 'root'@'localhost' IDENTIFIED BY '386mysql.';

> FLUSH PRIVILEGES;

or
> UPDATE mysql.user SET authentication_string = PASSWORD('386mysql.')
WHERE User = 'root' AND Host = 'localhost';
FLUSH PRIVILEGES;

mysql.server start
mysql.server stop

~~~


http://www.cnblogs.com/doctorJoe/p/5337510.html
