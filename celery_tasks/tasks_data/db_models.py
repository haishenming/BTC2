'''
Created on 2017年12月05日 下午12:41

@author: xiangyufan@juwang.cn

'''
from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, Float, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Okex(Base):
    __tablename__ = "okex"
    id = Column(Integer, primary_key=True)
    contract_id = Column(Integer, nullable=False)  # 合约ID
    last = Column(Float, nullable=False)  # 最新价：分
    buy = Column(Float, nullable=False)  # 买一价
    sell = Column(Float, nullable=False)  # 卖一价
    high = Column(Float, nullable=False)  # 最高价
    low = Column(Float, nullable=False)  # 最低价
    vol = Column(Float, nullable=False)  # 成交量
    unit_amount = Column(Float, nullable=False)  # 合约面值
    symbol = Column(String(16), nullable=False)
    # 类型 btc_usd   ltc_usd    eth_usd    etc_usd    bch_usd
    contract_type = Column(String(16), nullable=False)
    # 合约类型：this_week:当周 next_week:下周   quarter:季度
    date = Column(DateTime, nullable=False)
    future_index = Column(Float, nullable=False)  # 当前合约指数
    create_time = Column(DateTime, default=datetime.now)

class OkexPlus(Base):
    __tablename__ = "okex_plus"

    id = Column(Integer, primary_key=True)
    symbol = Column(String(16), nullable=False)
    X = Column(Float, nullable=False)    # 当周净利
    Y = Column(Float, nullable=False)    # 次周净利
    Z = Column(Float, nullable=False)    # 季度净利
    M = Column(Float, nullable=False)    # 次周为当周倍数
    N = Column(Float, nullable=False)    # 季度为次周倍数
    create_time = Column(DateTime, default=datetime.now)


class OkexNow(Base):
    __tablename__ = "okex_now"
    id = Column(Integer, primary_key=True)
    ticker_info = Column(Text)     # 信息
    index_info = Column(Text)     # 信息
    create_time = Column(DateTime, default=datetime.now)



