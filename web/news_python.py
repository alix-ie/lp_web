import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    except (requests.RequestException, ValueError):
        return False


def get_python_news():
    html = get_html('https://www.python.org/blogs/')

    try:
        soup = BeautifulSoup(html, 'html.parser')
        html_news = soup.find('ul', class_='list-recent-posts').findAll('li')

        result_news = []

        for news in html_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text

            result_news.append({
                'title': title,
                'url': url,
                'published': published,
            })
        return result_news

    except(TypeError, AttributeError):
        return False
