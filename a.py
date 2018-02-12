from BeautifulSoup import BeautifulSoup
import urllib2
 
url = 'https://portal.hanyang.ac.kr/GjshAct/viewRSS.do?gubun=rss'
handle = urllib2.urlopen(url)
data = handle.read()
soup = BeautifulSoup(data)
article = str( soup('div', {'class':'article',}) ) #div내의 article class 추출
print article.decode('utf8')
