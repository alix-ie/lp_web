from datetime import datetime

from bs4 import BeautifulSoup

from web.news.parsers.utils import get_html, save_news


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
