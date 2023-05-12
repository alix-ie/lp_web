from datetime import datetime

from sqlalchemy import func

from web import create_app
from web.db import db
from web.news.models import Comment, News
from web.user.models import User

app = create_app()


def show_hours():
    """
    Realise SQL request using sqlalchemy, for practice only.
    Doesn't make sense. Wasn't meant to make sense.

        select n.title,
            u.username,
            ROUND(SUM((julianday(datetime('now', 'localtime')) - julianday(c.created)) * 24)) as hours

        from news as n
        inner join comment as c
        on n.id = c.news_id

        inner join user as u
        on c.user_id = u.id

        group by n.title, u.username

    :return: str. Amount of hours passed since comment was created, summed for each user, grouped by news.
    """
    with app.app_context():
        query = db.session.query(
            News.title,
            User.username,
            func.round(func.sum((func.julianday(datetime.now()) - func.julianday(Comment.created)) * 24))
        ).join(
            Comment.news, Comment.user
        ).group_by(News.title, User.username)

        news_list = []
        with open('user_hours_per_news.txt', 'w') as f:
            for news, user, hours in query:
                if news not in news_list:
                    f.write(f'\n{news}:\n')
                    news_list.append(news)

                f.write(f'{user}: {hours}\n')


if __name__ == '__main__':
    show_hours()
