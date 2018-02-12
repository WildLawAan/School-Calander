import requests 
URL = 'http://www.tistory.com' 
response = requests.get(URL) 
response.status_code 
response.text

