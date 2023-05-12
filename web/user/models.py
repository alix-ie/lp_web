from flask_login import UserMixin
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash

from web.db import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    email = db.Column(db.String(50))

    comments = relationship('Comment', back_populates='user')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return f'User {self.id}: {self.username}'
