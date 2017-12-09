'''
Created on 2017年12月06日 下午2:23

@author: xiangyufan@juwang.cn

定时任务核心代码

'''
from datetime import datetime, timedelta

from apscheduler.schedulers.blocking import BlockingScheduler
from tasks_func import add_ticker, add_sdata_plus, get_sdata_list, get_ticker, \
    get_index, add_okex_plus_to_scv


def task_60s():
    """ 一分钟一次
    """
    print("############# 开始60s任务 #############")

    print("获取数据 ##########")
    sdata_list = get_sdata_list()
    parse_data = []
    for symbol, contract_type in sdata_list:
        rdata = get_ticker(symbol, contract_type)
        rdata_index = get_index(symbol)
        ticker = rdata["ticker"]
        parse_data.append((rdata, rdata_index, symbol, contract_type))

        print("写入原始数据 ########")
        add_ticker(rdata, rdata_index, symbol, contract_type)
    print("写入 统计数据 ############")
    add_sdata_plus(parse_data)

    print("############# 60s任务完成 #############")


def task_1d():
    """ 一天一次
    """
    print("############# 开始1d任务 #############")

    end = datetime.now()
    start = datetime.now() - timedelta(days=1)

    add_okex_plus_to_scv(start, end)
    print("写入excel")

    print("############# 1d任务完成 #############")


sched = BlockingScheduler()
sched.add_job(task_60s, 'interval', seconds=60)
sched.add_job(task_1d, 'interval', days=1)
sched.start()

