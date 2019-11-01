### 安装
~~~
pip install requests
~~~

### 导入
~~~
import requests
~~~

### 发送get请求
~~~
r = requests.get('http://www.baidu.com')
r.status_code #200
r.text
r.encoding
r.cookies
r.headers
r.headers['content-type']
~~~

### 发送post请求(自定义头部)
~~~
headers = { 'Authorization': 'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiI1YzA3MzdmZTExNGZhZDExMmM5NDg4YmMiLCJpYXQiOjE1NDc3OTQyNDEsImV4cCI6MTU0Nzk2NzA0MX0.BVBqJizBOqlnVa0xQvWsoAAAY9loBpjs7En0WapEA2Q' }
r = requests.post('http://api.xxx.cn/notes', headers=headers, data = {'title':'hello1','content':'hello','tags':'hello'})
r.status_code #200
~~~

### 发送delete请求(自定义头部)
~~~
r = requests.delete('http://api.xxx.cn/notes/5c417a9d9bc6b3248bac3cba' ,headers=headers )
r.status_code #200
r.json()
~~~

### 发送put请求(自定义头部)
~~~
r = requests.put('http://api.xxx.cn/notes', headers=headers, data = {'id':'5c417d339bc6b3248bac3cbb','title':'hello1','content':'hello1','tags':'hello1'})
r.status_code #200
~~~

### 发送get请求(带参数) 
~~~
r = requests.get('http://api.xxx.cn/notes', params={'id':'5c088665cc0e141e46580592'})
r.status_code #200
r.text
r.json()
~~~

### 文档
http://cn.python-requests.org/zh_CN/latest/

