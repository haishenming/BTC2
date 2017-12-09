from flask import render_template, redirect, url_for, abort, flash
from ..models import Okex
from .. import db

from . import main


######## db_model ###########

def get_new_okex(num=15):
    """ 获取最新的okex数据,可设置数量
    """

    return Okex.query.filter_by().order_by(Okex.create_time.desc()).limit(
        num).all()


####### views #########

@main.route('/')
def index():
    data = get_new_okex()


    return render_template('index.html')
