from bs4 import BeautifulSoup
import requests
import sqlite3
import time
from selenium import webdriver


def food_crawl_all():
    conn = sqlite3.connect('/home/jil8885/chatbot/database/food.db')
    cur = conn.cursor()
    cafeteria_list = ['-254','-255','-256','-257','-258']
    table_list = ['teacher','student','dorm','foodcourt','changbo']
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome('/home/jil8885/chatbot/crawler/chromedriver',chrome_options=options) 
    for number in range(5):
        x = cafeteria_list[number]
        sql = "delete from "+table_list[number]
        cur.execute(sql)
        driver.implicitly_wait(1)
        response = driver.get('http://www.hanyang.ac.kr/web/www/'+x)
        time.sleep(3)
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        food_list = soup.select('div > div > div > div > ul > li > a > h3')
        for x in food_list:
            text = x.string.strip()
            if text != '':
                title = text.split(']')[0] + ']' 
                content = text.split(']')[1]
                sql = "insert into "+table_list[number]+" (day,menu) values (?,?)"
                cur.execute(sql,(title,content))
    conn.commit()
    cur.close()
    conn.close()
food_crawl_all()
