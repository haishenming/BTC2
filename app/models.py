'''
Created on 2017年12月05日 下午12:41

@author: xiangyufan@juwang.cn

'''
from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, request
from flask_login import UserMixin, AnonymousUserMixin
from . import db, login_manager

class Okex(db.Model):
    __tablename__ = "okex"
    id = db.Column(db.Integer, primary_key=True)
    contract_id = db.Column(db.Integer, nullable=False)  # 合约ID
    last = db.Column(db.Float, nullable=False)  # 最新价：分
    buy = db.Column(db.Float, nullable=False)  # 买一价
    sell = db.Column(db.Float, nullable=False)  # 卖一价
    high = db.Column(db.Float, nullable=False)  # 最高价
    low = db.Column(db.Float, nullable=False)  # 最低价
    vol = db.Column(db.Float, nullable=False)  # 成交量
    unit_amount = db.Column(db.Float, nullable=False)  # 合约面值
    symbol = db.Column(db.String(16), nullable=False)
    # 类型 btc_usd   ltc_usd    eth_usd    etc_usd    bch_usd
    contract_type = db.Column(db.String(16), nullable=False)
    # 合约类型：this_week:当周 next_week:下周   quarter:季度
    date = db.Column(db.DateTime, nullable=False)
    future_index = db.Column(db.Float, nullable=False)  # 当前合约指数
    create_time = db.Column(db.DateTime, default=datetime.now)

class OkexPlus(db.Model):
    __tablename__ = "okex_plus"

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(16), nullable=False)
    X = db.Column(db.Float, nullable=False)    # 当周净利
    Y = db.Column(db.Float, nullable=False)    # 次周净利
    Z = db.Column(db.Float, nullable=False)    # 季度净利
    M = db.Column(db.Float, nullable=False)    # 次周为当周倍数
    N = db.Column(db.Float, nullable=False)    # 季度为次周倍数
    create_time = db.Column(db.DateTime, default=datetime.now)