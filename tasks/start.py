'''
Created on 2017年12月06日 下午2:23

@author: xiangyufan@juwang.cn

定时任务核心代码

'''

from apscheduler.schedulers.blocking import BlockingScheduler
from tasks_func import add_ticker, add_sdata_plus, get_sdata_list, get_ticker, \
    get_index


def task_60s():
    """ 一分钟一次
    """
    sdata_list = get_sdata_list()
    parse_data = []
    for symbol, contract_type in sdata_list:
        rdata = get_ticker(symbol, contract_type)
        rdata_index = get_index(symbol)
        ticker = rdata["ticker"]
        parse_data.append((rdata, rdata_index, symbol, contract_type))

        add_ticker(rdata, rdata_index, symbol, contract_type)
    add_sdata_plus(parse_data)

def task_1d():
    """ 一天一次
    """


sched = BlockingScheduler()
sched.add_job(task_60s, 'interval', seconds=60)
sched.start()

