### 源代码

~~~
import os
import urllib.request

path = os.path.join(os.getcwd(),'temp')
if not os.path.exists(path):
  os.mkdir(path)

for number in range(20):
	number = number + 1
	index = ''
	if len(str(number)) < 2:
		index = '00' + str(number)
	else:
		index = '0' + str(number)

	url = 'http://wlog.cn/demo/waterfall/images/'+index+'.jpg'
	file = path + '/waterfall_' +index + '.jpg'
	print(url)
	urllib.request.urlretrieve(url,file)
~~~