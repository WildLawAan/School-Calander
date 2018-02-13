from bs4 import BeautifulSoup
import requests
import datetime
from dateutil import parser

#현재시간관리 
now = datetime.datetime.now()
tm = now.month
t1 = now.year
ty = str(t1)






def get_html(url):
	_html = ""
	resp = requests.get(url)
	if resp.status_code == 200:
		_html = resp.text
		return _html

#today_month






URL = "https://portal.hanyang.ac.kr/GjshAct/viewRSS.do?gubun=rss"
html = get_html(URL)
soup = BeautifulSoup(html, 'html.parser')


items = soup.find_all('item')


for item in items:
	a = (item.find('title').text)
	b = (item.find('pubdate').text)
	# print(a[11])

	dt = parser.parse(b)
	dm= dt.month
	dn = dt.day
	

	if ( ty in b):
		if( tm == dm or ( (tm==1 and dm==12) or tm -1 == dm)):

		
	
			if ('[서울' in a and 'ERICA' not in a) or '성동' in a or ('서울캠퍼스' in a) or ('마감' in a):
				continue
			print(str(dm) + "월 " + str(dn) + "일 ")
			print(a)
			
			print()

			

	# 	continue
	# if((a[1]=="서") and (a[3] =="캠") and (a[5]=="스")):
	# 	continue

	# if((a[1]=="서") and (a[2] =="울") and (a[5]=="스")):
	# 	continue
	



	 
	# print(item.find('pubdate').text)
	# print()

