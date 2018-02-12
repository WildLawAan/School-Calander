import requests
import websocket
import json

'''
봇한테 메세지가 입력되면 이 함수가 실행됨.
ws: 웹소켓 객체 
message: 입력받은 message, JSON 형태의 str
message 예시들 : 
"{'type': 'hello'}" => 클라이언트와 서버가 통신에 성공하면 서버가 전송하는 메세지
"{'type': 'user_typing', 'channel': 'C752U6T3M', 'user': 'U6ZJA9HD2'}" => 어떤 유저가 입력중일때
"{'type': 'message', 'channel': 'C752U6T3M', 'user': 'U6ZJA9HD2', 'text': '성학', 'ts': '1515752671.000147', 'source_team': 'T6RU0AESZ', 'team': 'T6RU0AESZ'}" => 입력한 메세지가 봇에게 전달됐을때
'''
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
   

token = 'xoxb-297830515171-pL49pH41WabIgJltsur1tdr2' # Bot Integration으로 등록 후 발급받은 Token, xoxb-아무-토큰 형태임
get_url = requests.get('https://slack.com/api/rtm.connect?token=' + token) # Slack RTM에 WebSocket 통신 URL을 가져오는 API 요청 보냄
'''
API Response 예시:
{
  "ok": true,
  "url": "wss://mpmulti-xxxx.lb.slack-msgs.com/websocket/매우긴문자열/2?dp=1",
  "team": {
    "id": "T6RU0AESZ",
    "name": "Jaram Academy",
    "domain": "jaram-academy"
  },
  "self": {
    "id": "봇ID",
    "name": "봇이름"
  }
}
'''

socket_endpoint = get_url.json()['url'] # get_url.json()은 위의 JSON 객체 형태를 지니니까, 여기서 ULR 부분만 뽑아와서 socket_endpoint에 저장

websocket.enableTrace(True) # 디버깅을 위해 통신 정보를 모두 콘솔에 프린트 
ws = websocket.WebSocketApp(socket_endpoint, on_message=on_message) # 가져온 URL, 콜백 함수를 이용하여 WebSocket 객체 생성
ws.run_forever() # WebSocket 서버와 통신
