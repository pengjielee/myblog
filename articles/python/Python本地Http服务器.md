在 Linux 服务器上或安装了 Python 的机器上，Python自带了一个WEB服务器 SimpleHTTPServer，我们可以很简单的使用  python -m SimpleHTTPServer 快速搭建一个http服务，提供一个文件浏览的web服务，而mac自带了 python，windows需要安装python才能使用。

1. 当前目录发布到8001端口(明令后边的8001端口是可选的，不设置的话使用默认端口8000)，该服务是前台运行的，control+c会关闭该服务。
~~~
# python2.x
python -m SimpleHTTPServer 8001

# python3.x
python3 -m http.server 8001
~~~

2. 进程在后台运行，control+c不会关闭该服务，关闭bash时关闭服务。
~~~
python -m SimpleHTTPServer 8001 &
~~~

3. 在命令的开头加一个nohup，忽略所有的挂断信号，如果当前bash关闭，则当前进程会挂载到init进程下，成为其子进程，这样即使退出当前用户，其8000端口也可以使用。
~~~
nohup python -m SimpleHTTPServer 8001 &
~~~

4. 在浏览器访问：http://localhost:8001，如果当前文件夹有index.html文件，会默认显示该文件，否则，会以文件列表的形式显示目录下所有文件。