from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from web.news.models import News


class AddCommentForm(FlaskForm):
    news_id = HiddenField('News id', validators=[DataRequired()])
    comment_text = StringField('Comment', validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Send', render_kw={'class': 'btn btn-primary'})

    def validate_news_id(self, news_id):
        if not News.query.get(news_id.data):
            raise ValidationError('You are trying to leave a comment to a non-existent article')
