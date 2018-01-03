'''
Created on 2017年12月06日 下午2:24

@author: xiangyufan@juwang.cn

任务列表
'''
import csv
import time
import json
from datetime import datetime, timedelta

import os
import requests
from tasks_data.db_models import Okex, OkexPlus, OkexNow
from tasks_data.db_func import merge_record, get_okex_plus_by_time

# 获取OKEX合约行情
FUTURE_TICKER_URL = 'https://www.okex.com/api/v1/future_ticker.do'

# 获取OKEX合约指数信息
FUTURE_INDEX_URL = 'https://www.okex.com/api/v1/future_index.do'

# 获取okex现货信息
TICKER_NOW_URL = 'https://www.okex.com/api/v1/ticker.do'

# 合约参数
SDATA = (
    ('btc_usd', 'ltc_usd', 'eth_usd', 'etc_usd', 'bch_usd'),
    ('this_week', 'next_week', 'quarter')
)

# 现货参数
SDATA_NOW = (
    'ltc_btc', 'eth_btc', 'etc_btc', 'bch_btc', 'btc_usdt', 'eth_usdt',
    'ltc_usdt', 'etc_usdt', 'bch_usdt', 'etc_eth', 'bt1_btc', 'bt2_btc',
    'btg_btc', 'qtum_btc', 'hsr_btc', 'neo_btc', 'gas_btc', 'qtum_usdt',
    'hsr_usdt', 'neo_usdt', 'gas_usdt'
)

# 请求超时时间
TIMEOUT = 5


def get_ticker(symbol, contract_type):
    """ 获取ticker
    """
    data = {
        "symbol": symbol,
        "contract_type": contract_type
    }

    response = requests.get(FUTURE_TICKER_URL, params=data, timeout=TIMEOUT)

    rdata = response.json()

    return rdata

def get_index(symbol):
    """ 获取index
    """
    data = {
        "symbol": symbol,
    }

    response = requests.get(FUTURE_INDEX_URL, params=data, timeout=TIMEOUT)

    rdata = response.json()

    return rdata

def get_ticker_now(symbol):
    """ 获取现货信息
    """
    data = {
        "symbol": symbol,
    }

    response = requests.get(TICKER_NOW_URL, params=data, timeout=TIMEOUT)

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
    print("############# 写入原始数据 #############")
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
    symbols = SDATA[0]
    contract_types = SDATA[1]
    group_by_symbol = {}
    for symbol in symbols:
        group_by_symbol[symbol] = {}
        for data in parse_data:
            if data[2] == symbol:
                group_by_symbol[symbol][data[3]] = data

    print(group_by_symbol)
    rdata = {}
    for k, v in group_by_symbol.items():
        for d in v:
            this_week = v["this_week"]
            next_week = v["next_week"]
            quarter = v["quarter"]

            A = this_week[0]["ticker"]["last"]
            B = next_week[0]["ticker"]["last"]
            C = quarter[0]["ticker"]["last"]
            D = this_week[1]["future_index"]

            X = A/D-1
            Y = B/D-1
            Z = C/D-1

            M = Y/X if X*Y > 0 else (Y-X)/abs(X)
            N = Z/Y if Z*Y > 0 else (Z-Y)/abs(Y)

            rdata[k] = {
                "A": A,
                "B": B,
                "C": C,
                "D": D,
                "X": X,
                "Y": Y,
                "Z": Z,
                "M": M,
                "N": N
            }

    print(rdata)
    return rdata

def add_sdata_plus(parse_data):
    """ 将解析后的sdata存入数据库
    """
    rdata = parse_sdata_list(parse_data)

    for k, v in rdata.items():
        okex_plus = OkexPlus(
            symbol=k,
            X=v["X"],
            Y=v["Y"],
            Z=v["Z"],
            M=v["M"],
            N=v["N"]
        )

        merge_record(okex_plus)

def add_okex_plus_to_scv(start, end):
    """ 添加okex到csv
    """
    okex_pluss = get_okex_plus_by_time(start, end)

    data = [["", "X.当周毛利", "Y.次周毛利", "Z.季度毛利", "M．次周为当周倍数",
             "N．季度为次周倍数", "添加时间"]]
    for op in okex_pluss:
        data.append([
            op.symbol,
            round(float(op.X), 8),
            round(float(op.Y), 8),
            round(float(op.Z), 8),
            round(float(op.M), 8),
            round(float(op.N), 8),
            op.create_time.strftime("%Y-%m-%d %H:%M:%S")
        ])
    filename = '合约'
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if not os.path.exists(base_path):
        os.mkdir(base_path)
    filename += "_%s.csv" % datetime.now().strftime('%Y%m%d')

    with open(os.path.join(base_path, "excel", filename), 'w', newline='',
              encoding='gb18030') as f:
        spam_writer = csv.writer(f)
        spam_writer.writerows(data)



def add_ticker_now():
    """ 将现货信息存入数据库
    """
    ticker_info = {}
    print("开始获取现货信息")
    for symbol in SDATA_NOW:
        print("获取 {} 现货".format(symbol))
        ticker_now = get_ticker_now(symbol)
        print(ticker_now)
        ticker_info[symbol] = ticker_now["ticker"]["last"]
    index_info = {}
    print("获取现货对应的index数值")
    for symbol in SDATA[0]:
        print("获取 {} index".format(symbol))
        index_now = get_index(symbol)
        print(index_now)
        index_info[symbol] = index_now["future_index"]

    okex_now = OkexNow(
        ticker_info=json.dumps(ticker_info),
        index_info = json.dumps(index_info)
    )
    print("现货信息写入数据库")
    merge_record(okex_now)


def task_10s():
    """ 10秒运行一次
    """
    start = time.time()
    print("############# 开始10s任务 #############")

    print("获取数据 ##########")
    sdata_list = get_sdata_list()
    parse_data = []
    for symbol, contract_type in sdata_list:
        print("获取 {} 合约信息 {}".format(symbol, contract_type))
        rdata = get_ticker(symbol, contract_type)
        rdata_index = get_index(symbol)
        ticker = rdata["ticker"]
        parse_data.append((rdata, rdata_index, symbol, contract_type))

        print("写入原始数据 ########")
        add_ticker(rdata, rdata_index, symbol, contract_type)
    print("写入 统计数据 ############")
    add_sdata_plus(parse_data)
    add_ticker_now()

    print("############# 10s任务完成 耗时 {} 秒 #############".
          format(time.time() - start))



def task_1d():
    """ 每天0点运行
    """
    print("############# 开始1d任务 #############")

    end = datetime.now()
    start = datetime.now() - timedelta(days=1)

    add_okex_plus_to_scv(start, end)
    print("写入excel")

    print("############# 1d任务完成 #############")



if __name__ == '__main__':
    pass
    # sdata_list = get_sdata_list()
    # parse_data = []
    # for symbol, contract_type in sdata_list:
    #     rdata = get_ticker(symbol, contract_type)
    #     rdata_index = get_index(symbol)
    #     ticker = rdata["ticker"]
    #     parse_data.append((rdata, rdata_index, symbol, contract_type))
    #
    #     add_ticker(rdata, rdata_index, symbol, contract_type)
    # add_sdata_plus(parse_data)
    # end = datetime.now()
    # start = datetime.now() - timedelta(days=1)
    #
    # add_okex_plus_to_scv(start, end)

    # add_ticker_now()

