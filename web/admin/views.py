from flask import Blueprint, render_template

from web.user.decorators import admin_required

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
@admin_required
def admin_index():
    title = 'Control Panel'
    return render_template(
        'admin/index.html',
        page_title=title
    )
