from flask import Flask, render_template

from web.news_python import get_python_news
from web.weather import weather_by_city


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route("/")
    def index():
        page_title = 'News Python'
        weather_report = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news = get_python_news()
        return render_template('index.html', page_title=page_title, weather=weather_report, news_list=news)

    return app
