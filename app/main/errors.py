from flask import render_template
from . import main


@main.app_errorhandler(403)
def forbidden(e):
    return render_template('error_page/403.html'), 403


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('error_page/404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('error_page/500.html'), 500
