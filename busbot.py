import requests
import websocket
import json

bus = '''
2017/12/20 기준 - 
:bus:*평일/안산 출발* :point_right: 05:50 - 06:10 - 06:35 - 06:50 - 07:05 - 07:20 - 07:40 - 08:15 - 08:50 - 09:20 - 09:50 - 10:20 - 10:50 - 11:20 - 11:50 - 12:15 - 12:40 - 13:10 - 13:40 - 14:10 - 14:40 - 15:10 - 15:40 - 16:05 - 16:30 - 16:50 - 17:10 - 17:30 - 17:55 - 18:25 - 18:55 - 19:25 - 19:50 - 20:20 - 20:50 - 21:20 - 22:00 - 22:40 
:oncoming_bus: *토요일/안산 출발* :point_right: 5:50 6:30 7:10 7:50 8:35 9:20 10:05 10:50 11:35 12:20 13:05 13:50 14:35 15:20 16:05 16:50 17:40 18:25 19:10 19:55 20:40 21:25 22:10 22:40
:trolleybus: *공휴일 및 일요일/안산 출발* :point_right: 5:50 6:50 7:50 8:50 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00 18:00 19:00 20:00 21:00 22:00 22:40 
http://www.kwbus.co.kr/index/bbs/board.php?bo_table=comm_01'''
def on_message(ws, message):
    message = json.loads(message)
    print(message)
    if 'type' in message.keys() and message['type'] != 'message':
        return 
    if '3102' in message['text']: # 메세지에 3102라는 단어가 포함되어 있으면, 3102 시간표를 채널 혹은 DM에 전송해 줌
        return_msg = {
            'channel': message['channel'],
            'type': 'message',
            'text': bus # 위에서 설정한 버스 시간표 텍스트
        }
        ws.send(json.dumps(return_msg))

token = 'xoxb-297830515171-pL49pH41WabIgJltsur1tdr2'
get_url = requests.get('https://slack.com/api/rtm.connect?token=' + token)
print(get_url.json()['url'])
socket_endpoint = get_url.json()['url']
print('Connecting to', socket_endpoint)

websocket.enableTrace(True)
ws = websocket.WebSocketApp(socket_endpoint, on_message=on_message)
ws.run_forever()
