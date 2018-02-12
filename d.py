from bs4 import BeautifulSoup
import requests



def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html

 
URL ="http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=tue&page={}"

html = get_html(URL)
soup = BeautifulSoup(html, 'html.parser')


webtoon_list = list()
soup = BeautifulSoup(html, 'html.parser')
webtoon_area = soup.find("table",{"class": "viewList"}).find_all("td", {"class":"title"})
print(webtoon_area)

n = len(soup)
print(n)



