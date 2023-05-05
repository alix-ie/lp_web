from urllib.parse import urljoin, urlparse

from flask import request, url_for


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))

    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def get_redirect_target():
    default_referrer = url_for('news.index')

    for target in (request.values.get('next'), default_referrer):

        if not target:
            continue

        if is_safe_url(target):
            return target
