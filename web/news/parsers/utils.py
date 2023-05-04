import requests

from web.db import db
from web.news.models import News


def get_html(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.141 Mobile Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text

    except (requests.RequestException, ValueError):
        return False


def save_news(title, url, published):
    news_exist = News.query.filter(News.url == url).count()
    if not news_exist:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()
