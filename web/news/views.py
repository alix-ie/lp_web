from flask import Blueprint, current_app, render_template

from web.weather import weather_by_city
from web.news.models import News

blueprint = Blueprint('news', __name__)


@blueprint.route("/")
def index():
    title = 'News Python'
    weather_report = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    news = News.query.order_by(News.published.desc()).all()
    return render_template('index.html', page_title=title, weather=weather_report, news_list=news)
