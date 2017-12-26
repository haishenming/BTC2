'''
Created on 2017年12月06日 下午2:23

@author: xiangyufan@juwang.cn

定时任务核心代码

'''

import time

from datetime import datetime, timedelta

from apscheduler.schedulers.blocking import BlockingScheduler
from tasks_func import add_ticker, add_sdata_plus, get_sdata_list, get_ticker, \
    get_index, add_okex_plus_to_scv, add_ticker_now


def task_20s():
    """ 20秒运行一次
    """
    start = time.time()
    print("############# 开始20s任务 #############")

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

    print("############# 20s任务完成 耗时 {} 秒 #############".
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
    sched = BlockingScheduler()
    sched.add_job(task_20s, 'interval', seconds=20)    # 每20秒运行一次
    sched.add_job(task_1d, 'cron', hour=0, minute=0, second=0)   #
    # 每天0点运行
    sched.start()

