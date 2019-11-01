## 修改文件的权限
~~~
chmod [options] who operator permission file-list (符号模式)

chmod [options] mode file-list (绝对模式）

参数
file-list 是chmod需要修改权限的文件名或目录的路径名
~~~

## Linux中主要有两种改变权限的方法：

第一种：使用符号模式，例如：chmod a+x file，此处的a代表所有用户，+代表添加权限，x代表执行权限
第二种：使用绝对模式，例如：chmod 777 file，表示为所有用户添加可读可写可执行权限，三个数值分别对应三种用户类型

1、符号模式

a. who 用户类型
~~~
who	用户类型	意义
u	  User	  文件的所有者
g	  Other	  与文件相关联的组
o	  Other	  所有其他用户
a	  All	    相当与ugo，所有用户
~~~

b. operator 运算符
~~~
operator	 意义
+	         为指定的用户类型添加权限
-	         为指定的用户类型删除权限
=	         设定或重置指定用户类型的权限
~~~

c. permission 模式
~~~
permission	意义	        对文件含义	         对目录含义
r	          设置读权限	  可以查看文件内容	     可以列出目录中的内容
w	          设置写权限	  可以修改文件内容	     可以在目录中创建、删除文件
x	          设置执行权限	可以执行文件	       可以进入目录
~~~ 

从上面可以知道，为什么在目录的权限中，r和x经常在一起设置，因为必须进入目录才能读取内容。


2、绝对模式

绝对模式的典型范例
~~~
模式	意义
777	所有用户都对文件具有读、写和执行权限
755	文件所有者对文件具有读、写和执行权限;组用户和其他用户对文件需有读和执行权限
711	文件所有者对文件具有读、写和执行权限;组用户和其他用户对文件具有执行权限
644	文件所有者可以读、写文件;组用户和其他用户可以读文件
640	文件所有者可以读、写文件;组用户可以读文件;其他用户不能访问文件
 
选项
-c                 显示修改过程信息
-f                 强制修改权限
-R                 对目录递归修改权限
-v                 显示修改过后的的信息
~~~

示例

a. 此处为文件所有者添加执行权限，列出文件详细信息，可看到开头有-rw-r--r--，排除第一位，后面的每三位代表一种用户类型，-表示无设置
~~~
$ chmod u+x
$ ls -l temp 
-rw-r--r-- 1 siu siu 0  1月 10 13:50 temp

$ chmod u+x temp 
$ ls -l temp 
-rwxr--r-- 1 siu siu 0  1月 10 13:50 temp
~~~

b. 为文件所有者和组用户添加执行权限
~~~
$ chmod ug+x
$ ls -l temp 
-rwxr--r-- 1 siu siu 0  1月 10 13:50 temp

$ chmod ug=rwx temp 
$ ls -l temp 
-rwxrwxr-- 1 siu siu 0  1月 10 13:50 temp
~~~

c. 为组用户减去执行权限
~~~
$ chmod g-x
$ ls -l temp 
-rwxrwxr-- 1 siu siu 0  1月 10 13:50 temp

$ chmod g-x temp 
$ ls -l temp 
-rwxrw-r-- 1 siu siu 0  1月 10 13:50 temp
~~~

d. 为所有用户添加可读可写可执行权限
~~~
$ chmod 777
$ ls -l temp 
-rwxrw-r-- 1 siu siu 0  1月 10 13:50 temp

$ chmod 777 temp 
$ ls -l temp 
-rwxrwxrwx 1 siu siu 0  1月 10 13:50 temp
~~~
 
e. 为所有者添加读、写和执行权限，组用户和其他用户添加读和执行权限
~~~
$ chmod 755

$ ls -l temp 
-rwxrwxrwx 1 siu siu 0  1月 10 13:50 temp

$ chmod 755 temp 
$ ls -l temp 
-rwxr-xr-x 1 siu siu 0  1月 10 13:50 temp
~~~

f. 递归为文件夹添加权限，并显示权限添加信息
~~~
$ chmod -Rv 755
$ ls -l
总用量 4
drwxr-xr-x 2 siu siu 4096  1月 10 13:57 dir

$ chmod -Rv 755 dir
"dir" 的权限模式保留为0755 (rwxr-xr-x)
~~~

Tips
1.文件夹必须先要有执行权限才可读写
2.除了以上基本的用户权限外，还有setuid、setgid和粘滞位等设置，有点高级。
