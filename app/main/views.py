from flask import render_template, redirect, url_for, abort, flash

from app.main.comm_func import get_symbol_dic_config
from ..models import Okex
from .. import db
from manage import app
from .db_model import get_new_okexs_by_symbol

from . import main

SYMBOL_DIC = get_symbol_dic_config()


####### views #########

@main.route('/')
def index():
    symbol_dic = SYMBOL_DIC

    okexs = get_new_okexs_by_symbol("btc_usd")



    return render_template('index.html')
