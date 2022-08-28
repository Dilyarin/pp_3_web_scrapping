import bs4
import requests
from bs4 import BeautifulSoup

HEADERS =  {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '_ym_d=1653336334; _ym_uid=1653336334597414991; hl=ru; fl=ru; _ga=GA1.2.750197968.1653336334; habr_web_home_feed=/all/; _ym_isad=2; _gid=GA1.2.379245050.1661671560',            'Host': 'habr.com',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'sec-gpc': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/}',
            }

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/all/', headers = HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all(class_='tm-article-snippet')
for article in articles:
    date = article.find(class_ ='tm-article-snippet__datetime-published')
    tag_b = article.find('h2')
    tag_a = article.find('h2').find('a')
    href = tag_a.attrs['href']
    url = 'https://habr.com' + href
    for keyword in KEYWORDS:
        if keyword in article.text:
            print(date.text, '-',  tag_a.text, '-', url)

