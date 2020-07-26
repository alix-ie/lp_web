from datetime import datetime

import requests
from bs4 import BeautifulSoup

from web.db import db
from web.news.models import News


def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    except (requests.RequestException, ValueError):
        return False


def get_python_news():
    html = get_html('https://www.python.org/blogs/')

    if html:
        soup = BeautifulSoup(html, 'html.parser')
        html_news = soup.find('ul', class_='list-recent-posts').findAll('li')

        for news in html_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text

            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except ValueError:
                published = datetime.now()

            save_news(title, url, published)


def save_news(title, url, published):
    news_exist = News.query.filter(News.url == url).count()
    if not news_exist:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()
