### 源代码
~~~
# datetime: 2019.01.24
# filename: spider.py

import sys
import requests
from bs4 import BeautifulSoup
import csv

total = 0
outfile = ''

def format(text):
	text = text.replace(',',' ').strip()
	return text

def saveData(houses):
	global outfile
	with open(outfile+'.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for house in houses:
			writer.writerow(house)
		global total
		total = total + len(houses)
		print(str(total) + ' saved.')

def getHtml(url):
	print(url)
	headers = { 'User-Agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' }
	html = requests.get(url,headers=headers).text
	soup = BeautifulSoup(html, 'html.parser')
	houses = []
	for li in soup.select('.sellListContent li.LOGCLICKDATA'):
		item = []
		title = li.select('.title')[0].find('a').get_text()
		href  = li.select('.title')[0].find('a').get('href')
		info = li.select('.houseInfo')[0].get_text()
		position = li.select('.positionInfo')[0].get_text()
		follow = li.select('.followInfo')[0].get_text()
		totalPrice = li.select('.totalPrice')[0].get_text()
		unitPrice = li.select('.unitPrice')[0].get_text()
		tags = li.select('.tag')[0].get_text()
		item.append(format(title))
		item.append(format(href))
		item.append(format(info))
		item.append(format(position))
		item.append(format(follow))
		item.append(format(totalPrice))
		item.append(format(unitPrice))
		item.append(format(tags))
		houses.append(item)
	saveData(houses)

def main(argv):
	global outfile
	host = len(argv) >= 2 and argv[1] or 'https://zz.lianjia.com/ershoufang/pg'
	outfile = len(argv) >= 3 and argv[2] or 'zhenzhou'
	for page in range(100):
		url =  host + str(page+1) + "/"
		getHtml(url)

if __name__ == "__main__":
	main(sys.argv)
~~~

### 使用
~~~
// 默认抓取郑州二手房数据
python3 spider.py

// 抓取北京二手房数据
python3 spider.py https://bj.lianjia.com/ershoufang/pg beijing
~~~
