### 查看系统信息
~~~
输入"uname -a ",可显示电脑以及操作系统的相关信息。

输入"cat /proc/version",说明正在运行的内核版本。

输入"cat /etc/issue", 显示的是发行版本信息
~~~

### 下载网络文件（wget/curl）

a. wget是linux下一个从网络上自动下载文件的常用自由工具。它支持HTTP，HTTPS和FTP协议，可以使用HTTP代理。一般的使用方法是: wget + 空格 + 参数 + 要下载文件的url路径。

~~~
wget -c https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.4.9.tgz

wget常用参数:
-b：后台下载，Wget默认的是把文件下载到当前目录。
-O：将文件下载到指定的目录中。
-P：保存文件之前先创建指定名称的目录。
-t：尝试连接次数，当Wget无法与服务器建立连接时，尝试连接多少次。
-c：断点续传，如果下载中断，那么连接恢复时会从上次断点开始下载。
-r：使用递归下载ls
~~~

b. cURL是在多种协议上传输数据的命令行工具。cURL是支持FTP, HTTP, FTPS, TFTP, TELNET, IMAP, POP3等协议的客户端应用。cURL是一个不同于wget 的简单下载器，和其它的相比，它支持LDAP，POP3。cURL也很好的支持代理下载，暂停下载以及恢复下载。

~~~
curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.0.6.tgz    # 下载
tar -zxvf mongodb-linux-x86_64-3.0.6.tgz                                   # 解压
mv  mongodb-linux-x86_64-3.0.6/ /usr/local/mongodb                         # 将解压包拷贝到指定目录
export PATH=<mongodb-install-directory>/bin:$PATH                          # 将其添加到 PATH 路径中
~~~

### 重命名文件/目录（mv/rename）

在Linux下重命名文件或目录，可以使用mv命令或rename命令，这里分享下二者的使用方法。

mv命令既可以重命名，又可以移动文件或文件夹。
~~~
例子：将目录A重命名为B
mv A B

例子：将/a目录移动到/b下，并重命名为c
mv /a /b/c
~~~

其实在文本模式中要重命名文件或目录，只需要使用mv命令就可以了，比如说要将一个名为abc的文件重命名为1234：
~~~
mv abc 1234
~~~
注意，如果当前目录下也有个1234的文件的话，这个文件是会将它覆盖的。

### 压缩/解压（zip/unzip）
~~~
1、把/home目录下面的mydata目录压缩为mydata.zip
zip -r mydata.zip mydata #压缩mydata目录

2、把/home目录下面的mydata.zip解压到mydatabak目录里面
unzip mydata.zip -d mydatabak

3、把/home目录下面的abc文件夹和123.txt压缩成为abc123.zip
zip -r abc123.zip abc 123.txt

4、把/home目录下面的wwwroot.zip直接解压到/home目录里面
unzip wwwroot.zip

5、把/home目录下面的abc12.zip、abc23.zip、abc34.zip同时解压到/home目录里面
unzip abc\*.zip

6、查看把/home目录下面的wwwroot.zip里面的内容
unzip -v wwwroot.zip

7、验证/home目录下面的wwwroot.zip是否完整
unzip -t wwwroot.zip

8、把/home目录下面wwwroot.zip里面的所有文件解压到第一级目录
unzip -j wwwroot.zip
~~~

主要参数
-c：将解压缩的结果
-l：显示压缩文件内所包含的文件
-p：与-c参数类似，会将解压缩的结果显示到屏幕上，但不会执行任何的转换
-t：检查压缩文件是否正确
-u：与-f参数类似，但是除了更新现有的文件外，也会将压缩文件中的其它文件解压缩到目录中
-v：执行是时显示详细的信息
-z：仅显示压缩文件的备注文字
-a：对文本文件进行必要的字符转换
-b：不要对文本文件进行字符转换
-C：压缩文件中的文件名称区分大小写
-j：不处理压缩文件中原有的目录路径
-L：将压缩文件中的全部文件名改为小写
-M：将输出结果送到more程序处理
-n：解压缩时不要覆盖原有的文件
-o：不必先询问用户，unzip执行后覆盖原有文件
-P<密码>：使用zip的密码选项
-q：执行时不显示任何信息
-s：将文件名中的空白字符转换为底线字符
-V：保留VMS的文件版本信息
-X：解压缩时同时回存文件原来的UID/GID

