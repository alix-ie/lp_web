from flask import abort, Blueprint, current_app, flash, redirect, render_template
from flask_login import current_user, login_required

from web.db import db
from web.news.forms import AddCommentForm
from web.news.models import Comment, News
from web.utils import flash_form_errors, get_redirect_target
from web.weather import get_weather

blueprint = Blueprint('news', __name__)


@blueprint.route("/")
def index():
    title = 'News Python'
    weather = get_weather(current_app.config['WEATHER_DEFAULT_CITY'])
    news = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).limit(10).all()

    return render_template(
        'news/index.html',
        page_title=title,
        weather=weather,
        news_list=news
    )


@blueprint.route('/news/<int:news_id>')
def single_news(news_id):
    news = News.query.filter(News.id == news_id).first()
    add_comment_form = AddCommentForm(news_id=news.id)

    if not news:
        abort(404)

    return render_template(
        'news/single_news.html',
        page_title=news.title,
        news=news,
        add_comment_form=add_comment_form
    )


@blueprint.route('/news/add-comment', methods=['POST'])
@login_required
def add_comment():
    form = AddCommentForm()

    if form.validate_on_submit():
        new_comment = Comment(
            text=form.comment_text.data,
            news_id=form.news_id.data,
            user_id=current_user.id
        )
        db.session.add(new_comment)
        db.session.commit()
        flash('Comment was added successfully.')

    else:
        flash_form_errors(form)

    return redirect(get_redirect_target())
