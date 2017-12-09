import json

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

    return render_template('index.html')

@main.route('/okex')
def get_okex():
    """ 获取okex
    """
    pass
    symbol_dic = SYMBOL_DIC
    rdata = []
    for k, v in symbol_dic.items():
        okexs = get_new_okexs_by_symbol(symbol=v, num=3)
        data = {}
        for okex in okexs:
            data.update({
                okex.contract_type: okex.last,
                "future_index": okex.future_index,
                "symbol": k
            })
        rdata.append(data)
    return json.dumps(rdata)


@main.route('/okex_plus')
def get_okex_plus():
    """ 获取okex统计数据
    """
    pass
