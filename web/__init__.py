from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from web.db import db
from web.admin.views import blueprint as admin_blueprint
from web.news.views import blueprint as news_blueprint
from web.user.models import User
from web.user.views import blueprint as user_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
