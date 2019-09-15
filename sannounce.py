from bs4 import BeautifulSoup
import requests

from datetime import datetime
from dateutil import parser
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler

#현재시간관리 
now = datetime.now()
tm = now.month
t1 = now.year
ty = str(t1)
update_date = None
fin_title = None






def get_html(url):
	_html = ""
	resp = requests.get(url)
	if resp.status_code == 200:
		_html = resp.text
		return _html

#today_month

def on_message(ws, message):
    message = json.loads(message) # 전달받은 message는 무조건 JSON 형태이므로, 이를 사용하기 쉽게 Python Dict 형식으로 변환 
    if 'type' not in message.keys() or message['type'] != 'message': # 입력받은 메세지가 텍스트가 아닐 경우
        return # 여기서 다룰 필요가 없으므로 그냥 끝내기

    return_msg = { 
        'channel': message['channel'], # 메세지를 입력한 채널에 다시 전송해야 하니까 그대로 가져다 쓰기
        'type': 'message', # 메세지를 전송하니까 message 형태
        'text': message['text'] # 전달할 메세지, echo 봇이니까 들어온 메세지를 그대로 다시 전달 
    }
    ws.send(json.dumps(return_msg)) # 서버에 메세지를 전송 

def watcher():
	global update_date, fin_title

	URL = "https://portal.hanyang.ac.kr/GjshAct/viewRSS.do?gubun=rss"
	html = get_html(URL)
	soup = BeautifulSoup(html, 'html.parser')
	link1 = soup.link.next_sibling.strip()
	
	items = soup.find_all('item')
	

	# Tue, 13 Feb 2018 15:00:00 GMT
	for item in items:
		title = (item.find('title').text)
		link2 = item.link.next_sibling.strip()
		pubdate = (item.find('pubdate').text)
		
		# str_date = parser.parse(pubdate)
		pubdate_obj = datetime.strptime(pubdate, '%a, %d %b %Y %H:%M:%S %Z')

		# if ('[서울' in title and 'ERICA' not in title) or '성동' in title or ('서울캠퍼스' in title) or ('마감' in title):
		# 	break

		print(update_date)
		# TODO: 타이틀이 다를 때도 비교해 줘야함
		if not update_date or update_date < pubdate_obj or (fin_title != title):
			update_date = pubdate_obj
			# print("title") 
			fin_title = title
			send_to_slack(title, link1 + link2)

		# print(title)			
		break

	# print("dt2: {}".format(str_date))


def send_to_slack(title, link):
	print("title: {}\nlink: {}".format(title, link))


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(watcher, 'interval', seconds=3)
    scheduler.start()

    token = os.environ.get('SLACK_BOT_TOKEN') # Bot Integration으로 등록 후 발급받은 Token, xoxb-아무-토큰 형태임
	get_url = requests.get('https://slack.com/api/rtm.connect?token=' + token) # Slack RTM에 WebSocket 통신 URL을 가져오는 API 요청 보냄

	socket_endpoint = get_url.json()['url'] # get_url.json()은 위의 JSON 객체 형태를 지니니까, 여기서 ULR 부분만 뽑아와서 socket_endpoint에 저장

    try:
    	websocket.enableTrace(True) # 디버깅을 위해 통신 정보를 모두 콘솔에 프린트 
		ws = websocket.WebSocketApp(socket_endpoint, on_message=on_message) # 가져온 URL, 콜백 함수를 이용하여 WebSocket 객체 생성
    	ws.run_forever() 
        # This is here to simulate application activity (which keeps the main thread alive).
        # while True:
        # 	time.sleep(2)
        	# ret_date = watcher()
        	# if watcher() != fin:
        	# 	fin = send_to_slack()
        		



    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()


		
