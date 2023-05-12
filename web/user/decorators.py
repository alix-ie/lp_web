from functools import wraps

from flask import flash, redirect
from flask_login import current_user, login_required

from web.utils import get_redirect_target


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_admin:
            flash("Sorry, you're not admin.")
            return redirect(get_redirect_target())
        return func(*args, **kwargs)

    return login_required(decorated_view)
