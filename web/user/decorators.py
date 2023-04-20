from functools import wraps

from flask import flash, redirect, url_for
from flask_login import current_user, login_required


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_admin:
            flash("Sorry, you're not admin.")
            return redirect(url_for('news.index'))
        return func(*args, **kwargs)

    return login_required(decorated_view)
