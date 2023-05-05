from datetime import datetime

from sqlalchemy.orm import relationship

from web.db import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)

    comments = relationship('Comment', back_populates='news')

    def comments_count(self):
        return len(self.comments)

    def __repr__(self):
        return '<News {} {}>'.format(self.title, self.url)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    news_id = db.Column(db.Integer, db.ForeignKey('news.id', ondelete='CASCADE'), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), index=True)

    news = relationship('News', back_populates='comments')
    user = relationship('User', back_populates='comments')

    def __repr__(self):
        return f'<Comment {self.id}>'
