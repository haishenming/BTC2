'''
Created on 2017年12月06日 下午2:24

@author: xiangyufan@juwang.cn

任务列表
'''
from datetime import datetime

import requests
from tasks_data.db_models import Okex
from tasks_data.db_func import merge_record

# 获取OKEX合约行情
FUTURE_TICKER_URL = 'https://www.okex.com/api/v1/future_ticker.do'

# 获取OKEX合约指数信息
FUTURE_INDEX_URL = 'https://www.okex.com/api/v1/future_index.do'

SDATA = (
    ('btc_usd', 'ltc_usd', 'eth_usd', 'etc_usd', 'bch_usd'),
    ('this_week', 'next_week', 'quarter')
)


def get_ticker(symbol, contract_type):
    """ 获取ticker
    """
    data = {
        "symbol": symbol,
        "contract_type": contract_type
    }

    response = requests.get(FUTURE_TICKER_URL, params=data)

    rdata = response.json()

    return rdata

def get_index(symbol):
    """ 获取index
    """
    data = {
        "symbol": symbol,
    }

    response = requests.get(FUTURE_INDEX_URL, params=data)

    rdata = response.json()

    return rdata

def get_sdata_list():
    """ 获取sdata列表
    """
    symbols = SDATA[0]
    contract_types = SDATA[1]

    ret = []
    for symbol in symbols:
        for contract_type in contract_types:
            ret.append((symbol, contract_type))

    return ret

def add_ticker(rdata, rdata_index, symbol, contract_type):
    """ 获取并写入ticker
    """

    ticker = rdata["ticker"]
    okex = Okex(
        contract_id=int(ticker["contract_id"]),
        last=float(ticker['last']),
        buy=float(ticker['buy']),
        sell=float(ticker['sell']),
        high=float(ticker['high']),
        low=float(ticker['low']),
        vol=float(ticker['vol']),
        unit_amount=float(ticker['unit_amount']),
        symbol=symbol,
        contract_type=contract_type,
        date=datetime.fromtimestamp(int(rdata['date'])),
        future_index=float(rdata_index['future_index'])
    )
    merge_record(okex)

def parse_sdata_list(parse_data):
    """ 将sdata解析为可使用的数据
    """
    # 分组
    pass

def add_sdata_plus(parse_data):
    """ 将解析后的sdata存入数据库
    """
    sdata_plus = parse_sdata_list(parse_data)


if __name__ == '__main__':
    sdata_list = get_sdata_list()
    parse_data = []
    for symbol, contract_type in sdata_list:
        rdata = get_ticker(symbol, contract_type)
        rdata_index = get_index(symbol)
        ticker = rdata["ticker"]
        parse_data.append((rdata, rdata_index, symbol, contract_type))

        # add_ticker(rdata, rdata_index, symbol, contract_type)
    add_sdata_plus(parse_data)

