from bs4 import BeautifulSoup
import requests



def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html


URL = "http://www.hanyang.ac.kr/web/www/-93?p_p_id=calendarView_WAR_eventportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_calendarView_WAR_eventportlet_action=view"
html = get_html(URL)
soup = BeautifulSoup(html, 'html.parser')
print(soup)
