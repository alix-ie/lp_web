from web import create_app
from web.news_python import get_python_news

app = create_app()
with app.app_context():
    get_python_news()