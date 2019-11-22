## 安装Nodejs

1、添加NodeSource到yum库
~~~
$ curl -sL https://rpm.nodesource.com/setup_10.x | sudo bash -
~~~

2、安装Nodejs
~~~
$ sudo yum install nodejs
~~~

3、检查Nodejs安装
~~~
$ node --version
~~~

## 安装Nginx

1、安装EPEL repository
~~~
$ sudo yum install epel-release  
~~~

2、安装Nginx
~~~
$ sudo yum install nginx
~~~

3、启动Nginx
~~~
$ sudo systemctl enable nginx
$ sudo systemctl start nginx
$ sudo systemctl status nginx
~~~

4、防火墙设置
~~~
$ sudo firewall-cmd --permanent --zone=public --add-service=http
$ sudo firewall-cmd --permanent --zone=public --add-service=https
$ sudo firewall-cmd --reload
~~~

5、检查Nginx安装

浏览器中访问你的ip地址，http://yourip

6、管理Nginx
~~~
$ sudo systemctl status nginx
$ sudo systemctl start nginx
$ sudo systemctl stop nginx
$ sudo systemctl restart nginx
$ sudo systemctl reload nginx
$ sudo systemctl enable nginx
$ sudo systemctl disable nginx
~~~

## 安装MySQL 8.0

1、开启MySQL 8.0 repository
~~~
$ sudo yum localinstall https://dev.mysql.com/get/mysql80-community-release-el7-1.noarch.rpm
~~~

2、安装MySQL 8.0
~~~
$ sudo yum install mysql-community-server
~~~

## 安装MySQL 5.7

1、开启MySQL 5.7 repository
~~~
$ sudo yum localinstall https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
~~~

2、安装MySQL 5.7
~~~
$ sudo yum install mysql-community-server
~~~

3、启动MySQL
~~~
$ sudo systemctl enable mysqld
$ sudo systemctl start mysqld
$ sudo systemctl status mysqld
~~~

4、设置密码
~~~
$ sudo grep 'temporary password' /var/log/mysqld.log
~~~

5、连接MySQL 
~~~
$ mysql -u root -p 
~~~

## 安装Ghost

1、下载Ghost
~~~
$ wget https://ghost.org/zip/ghost-latest.zip
~~~

2、更新yum/安装unzip
~~~
$ sudo yum update -y
$ sudo yum install unzip -y
~~~

3、解压ghost-latest.zip
~~~
$ sudo mkdir /var/www
$ sudo unzip -d /var/www/ghost ghost-latest.zip
~~~

4、安装Ghost
~~~
$ cd /var/www/ghost/
$ sudo npm install --production
~~~

5、配置Ghost
~~~
$ cd core/server/config/env/
$ vi config.production.json

{
     "url":"http://www.domainname.cn", //你的域名
     "database": {
        "client": "mysql",
        "connection": {
            "host"     : "127.0.0.1",
            "user"     : "mysql数据库用户名称",
            "password" : "mysql数据库用户密码",
            "database" : "mysql数据库名称"
        }
    },
    "paths": {
        "contentPath": "content/"
    },
    "logging": {
        "level": "info",
        "rotation": {
            "enabled": true
        },
        "transports": ["file", "stdout"]
    }
}
~~~

6、配置nginx
~~~
$ vi /etc/nginx/conf.d/ghost.conf

server {
  listen 80;
  server_name www.domainname.cn;
  location / {
    proxy_set_header HOST $host;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_pass         http://127.0.0.1:2368;
  }
}

//重启nginx服务
$ systemctl restart nginx.service 
~~~

7、
访问博客: http://www.domainname.cn
访问博客后台：http://www.domainname.cn/ghost

## 为Ghost服务创建单独用户

1、添加ghost用户
~~~
$ sudo adduser --shell /bin/bash ghost
~~~

2、设置目录权限
~~~
$ sudo chown -R ghost:ghost /var/www/ghost/
~~~

3、登录ghost
~~~
$ sudo su - ghost
~~~

4、启动ghost服务
~~~
$ cd /var/www/ghost
$ npm start --production
~~~

## 运行Ghost为系统服务

1、创建Ghost服务
~~~
$ sudo vi /etc/systemd/system/ghost.service

[Unit]
Description=Ghost
After=network.target

[Service]
Type=simple

WorkingDirectory=/var/www/ghost
User=ghost
Group=ghost

ExecStart=/usr/bin/npm start --production
ExecStop=/usr/bin/npm stop --production
Restart=always
SyslogIdentifier=Ghost

[Install]
WantedBy=multi-user.target
~~~

2、启动Ghost服务
~~~
$ sudo systemctl enable ghost.service
$ sudo sytemctl start ghost.service
~~~


参考：
how to install and configure ghost on centos 7   
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-ghost-on-centos-7   

CentOS 7下搭建Ghost 2.6.2博客的超详细教程  
https://art3mis.info/chao-xiang-xi-centos-7da-jian-ghost-2-6-2bo-ke-jiao-cheng/   

how to install node js on centos 7  
https://linuxize.com/post/how-to-install-node-js-on-centos-7/  

how to install nginx on centos 7  
https://linuxize.com/post/how-to-install-nginx-on-centos-7/ 

install mysql on centos 7
https://linuxize.com/post/install-mysql-on-centos-7/  