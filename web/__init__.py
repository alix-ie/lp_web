from flask import Flask, render_template

from web.forms import LoginForm
from web.weather import weather_by_city
from web.model import db, News


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")
    def index():
        title = 'News Python'
        weather_report = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title=title, weather=weather_report, news_list=news)

    @app.route('/login')
    def login():
        title = 'Authorization'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    return app
