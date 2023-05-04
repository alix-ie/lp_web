from web import create_app
from web.news.parsers import sitepoint

app = create_app()
with app.app_context():
    sitepoint.get_news_snippets()
    sitepoint.get_news_content()
