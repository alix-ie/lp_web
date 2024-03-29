from celery import Celery
from celery.schedules import crontab

from web import create_app
from web.news.parsers import sitepoint

flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379/0')


@celery_app.task
def load_sitepoint_snippets():
    with flask_app.app_context():
        sitepoint.load_news_snippets()


@celery_app.task
def load_sitepoint_content():
    with flask_app.app_context():
        sitepoint.load_news_content()


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/1'), load_sitepoint_snippets.s())
    sender.add_periodic_task(crontab(minute='*/1'), load_sitepoint_content.s())
