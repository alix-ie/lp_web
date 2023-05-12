import requests

from web import config
from web.db import db
from web.news.models import News


def get_html(url):
    headers = {'User-Agent': config.REQUESTS_USER_AGENT}

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
