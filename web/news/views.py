from flask import abort, Blueprint, current_app, render_template

from web.weather import weather_by_city
from web.news.models import News

blueprint = Blueprint('news', __name__)


@blueprint.route("/")
def index():
    title = 'News Python'
    weather_report = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    news = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).all()
    return render_template('news/index.html', page_title=title, weather=weather_report, news_list=news)


@blueprint.route('/news/<int:news_id>')
def single_news(news_id):
    news = News.query.filter(News.id == news_id).first()

    if not news:
        abort(404)

    return render_template('news/single_news.html', page_title=news.title, news=news)
