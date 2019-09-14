from bs4 import BeautifulSoup
import requests
import datetime



def get_html(url):
	_html = ""
	resp = requests.get(url)
	if resp.status_code == 200:
		_html = resp.text
		return _html

#today_month
now = datetime.datetime.now()
tm = now.month
i=1


URL = "http://www.hanyang.ac.kr/web/www/-93?p_p_id=calendarView_WAR_eventportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_calendarView_WAR_eventportlet_action=view"
html = get_html(URL)
soup = BeautifulSoup(html, 'html.parser')
#table에서 받아와 주고 
all=soup.find("table",{"class":"tables-board board-list no-thead bbs-board"})
#3월을 받아옴 
#while(i)

trs = all.find('tbody').find_all('tr')
for tr in trs:
	month = tr.find('div', {'class': 'school-month'}).text.strip()
	#그 달과 그 다음 달만 출력되도록 변경
	ps = tr.find_all('p')
	a = int(month[0])  
	if(a == tm or a == tm+1):
		for p in ps:

			(date, event) = p.find_all('span')
			
	        
			print(date.text)
			print(event.text)
			print()

# while(i!=13):
# 	month=all.find("div",{"class":"school-month"})

# 	f=(month.text).strip()
# 	a = int(f[0])



	

# 	if(1):

# 		allday=all.find("div",{"class":"school-desc-wrap"})
# 		p = allday.find_all('p')
# 		for p_ in p:
# 			(date, title) = p_.find_all('span')
# 			print('일자:', date.text)
# 			print('제목:', title.text)
# 			print()

# 	i=i+1








#content > table > tbody > tr:nth-child(5) > td.title
