from datetime import datetime

from bs4 import BeautifulSoup

from web import config
from web.db import db
from web.news.models import News
from web.news.parsers.utils import get_html, save_news


def load_news_snippets():
    html = get_html(config.SITEPOINT_URL + '/python/')

    if not html:
        return

    soup = BeautifulSoup(html, 'html.parser')
    html_news = soup.findAll('section', class_='s15xj7te')[1].findAll('article')

    for news in html_news:
        news_header = news.find('a', class_='t12xxw3g')

        title = news_header.text
        url = config.SITEPOINT_URL + news_header['href']
        published = news.find('time').text

        try:
            published = datetime.strptime(published, '%B %d, %Y')
        except ValueError:
            published = datetime.now()

        if title and url and published:
            save_news(title, url, published)


def load_news_content():
    news_without_text = News.query.filter(News.text.is_(None))

    for news in news_without_text:
        html = get_html(news.url)

        if not html:
            return

        soup = BeautifulSoup(html, 'html.parser')
        news_text = soup.find(
            'section',
            class_='Body-module--section--154bb space-y-6'
        ).find('div').decode_contents()

        if news_text:
            news.text = news_text
            db.session.add(news)
            db.session.commit()
