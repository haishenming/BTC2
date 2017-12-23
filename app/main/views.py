import json

from flask import render_template, redirect, url_for, abort, flash, request

from app.main.comm_func import get_symbol_dic_config
from ..models import Okex
from .. import db
from manage import app
from .db_model import get_new_okexs_by_symbol, get_new_okex_plus, get_new_okex_now

from . import main

SYMBOL_DIC = get_symbol_dic_config()


####### views #########

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/basic')
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


@main.route('/main')
def get_okex_plus():
    """ 获取okex统计数据
    """
    data = request.args
    x_num = {"max": data.get("x[max]"), "min": data.get("x[min]")}
    y_num = {"max": data.get("y[max]"), "min": data.get("y[min]")}
    z_num = {"max": data.get("z[max]"), "min": data.get("z[min]")}
    m_num = {"max": data.get("m[max]"), "min": data.get("m[min]")}
    n_num = {"max": data.get("n[max]"), "min": data.get("n[min]")}

    okex_pluss = get_new_okex_plus(5)

    rdata = []
    for okex_plus in okex_pluss:
        symbol = okex_plus.symbol
        X = okex_plus.X
        Y = okex_plus.Y
        Z = okex_plus.Z
        M = okex_plus.M
        N = okex_plus.N
        check_x = x_num["min"] != x_num["max"]
        check_y = y_num["min"] != y_num["max"]
        check_z = z_num["min"] != z_num["max"]
        check_m = m_num["min"] != m_num["max"]
        check_n = n_num["min"] != n_num["max"]
        msg = {
            "X": 1 if not(float(x_num["min"]) < X < float(x_num["max"]))
                      and check_x else 0,

            "Y": 1 if not(float(y_num["min"]) < Y < float(y_num["max"]))
                      and check_y else 0,

            "Z": 1 if not(float(z_num["min"]) < Z < float(z_num["max"]))
                      and check_z else 0,

            "M": 1 if not(float(m_num["min"]) < M < float(m_num["max"]))
                      and check_m else 0,

            "N": 1 if not(float(n_num["min"]) < N < float(n_num["max"]))
                      and check_n else 0,
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


@main.route("/additional")
def get_okex_now():
    """ 获取现货信息
    """

    datas = get_new_okex_now(num=1)
    data = datas[0]

    ticker_infos = json.loads(data.ticker_info)
    index_infos = json.loads(data.index_info)

    rdata = {}
    for symbol, index in index_infos.items():
        rdata[symbol] = {
            "ticker": ticker_infos.get(symbol + "t"),
            "{}_btc".format(symbol[0:3]): ticker_infos.get("{}_btc".format(symbol[0:3])) or 1,
            "index": index
        }

    return json.dumps(rdata)
