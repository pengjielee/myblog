### phpAdmin连接MySQL8.0报错
~~~
#2054 - The server requested authentication method unknown to the client
mysqli_real_connect(): The server requested authentication method unknown to the client [caching_sha2_password]
mysqli_real_connect(): (HY000/2054): The server requested authentication method unknown to the client
~~~

### 原因：
MYSQL8.0的密码验证方式从mysql_native_password改为了caching_sha2_password。

### 解决：
1. 修改密码认证方式：
~~~
vi /etc/my.cnf
# default_authentication_plugin=caching_sha2_password
default_authentication_plugin=mysql_native_password
~~~

2. 修改密码：
~~~
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '你的密码';  
FLUSH PRIVILEGES; 
~~~
