import json

from flask import render_template, redirect, url_for, abort, flash, request

from app.main.comm_func import get_symbol_dic_config
from ..models import Okex
from .. import db
from manage import app
from .db_model import get_new_okexs_by_symbol, get_new_okex_plus

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

    default = '{"max": 0, "min": 0}'
    x_num = json.loads(request.args.get("x", default))
    y_num = json.loads(request.args.get("y", default))
    z_num = json.loads(request.args.get("z", default))
    m_num = json.loads(request.args.get("m", default))
    n_num = json.loads(request.args.get("n", default))

    okex_pluss = get_new_okex_plus(5)

    rdata = []
    for okex_plus in okex_pluss:
        print(okex_plus.Z)
        symbol = okex_plus.symbol
        X = okex_plus.X
        Y = okex_plus.Y
        Z = okex_plus.Z
        M = okex_plus.M
        N = okex_plus.N
        msg = {
            "X": 1 if int(x_num["min"]) < X < int(x_num["max"]) else 0,
            "Y": 1 if int(y_num["min"]) < Y < int(y_num["max"]) else 0,
            "Z": 1 if int(z_num["min"]) < Z < int(z_num["max"]) else 0,
            "M": 1 if int(m_num["min"]) < M < int(m_num["max"]) else 0,
            "N": 1 if int(n_num["min"]) < N < int(n_num["max"]) else 0,
        }

        rdata.append({
            "symbol": symbol,
            "X": X,
            "Y": Y,
            "Z": Z,
            "M": M,
            "N": N,
            "msg": msg
        })

    return json.dumps(rdata)
