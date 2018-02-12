import requests
import websocket
import json
import random

msgs = None
with open('messages.json', 'r') as fr:
    msgs = json.loads(fr.read())
def on_message(ws, message):
    message = json.loads(message)
    print(message)
    if 'type' in message.keys() and message['type'] != 'message':
        return 
    for msg in msgs:
        for kwd in msg['kwds']:
            if kwd in message['text']:
                index = random.randrange(0, len(msg['text']))
                return_msg = {
                    'channel': message['channel'],
                    'type': 'message',
                    'text': msg['text'][index]
                }
                ws.send(json.dumps(return_msg))
                break

token = 'xoxb-너의토큰-아무토큰'
get_url = requests.get('https://slack.com/api/rtm.connect?token=' + token)
print(get_url.json()['url'])
socket_endpoint = get_url.json()['url']
print('Connecting to', socket_endpoint)

websocket.enableTrace(True)
ws = websocket.WebSocketApp(socket_endpoint, on_message=on_message)
ws.run_forever()
